// Torontle — a Wordle clone built entirely from this site's own slang data.
// Daily puzzle is the same for every visitor on a given UTC day (deterministic
// hash of the date), Practice mode is unlimited random rounds. No backend —
// everything lives in localStorage.

(function () {
  "use strict";

  const STATS_KEY = "torontle-stats-v1";
  const DAILY_KEY = "torontle-daily-v1";
  const PRACTICE_KEY = "torontle-practice-v1";

  const KEYBOARD_ROWS = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"],
  ];

  const els = {
    board: document.getElementById("board"),
    keyboard: document.getElementById("keyboard"),
    status: document.getElementById("wordle-status"),
    endPanel: document.getElementById("end-panel"),
    endTitle: document.getElementById("end-title"),
    endDef: document.getElementById("end-term-def"),
    endExample: document.getElementById("end-term-example"),
    endOrigin: document.getElementById("end-term-origin"),
    shareBtn: document.getElementById("share-btn"),
    viewLink: document.getElementById("view-dictionary-link"),
    practiceAgainBtn: document.getElementById("practice-again-btn"),
    tabDaily: document.getElementById("tab-daily"),
    tabPractice: document.getElementById("tab-practice"),
    statPlayed: document.getElementById("stat-played"),
    statWinPct: document.getElementById("stat-winpct"),
    statStreak: document.getElementById("stat-streak"),
    statMaxStreak: document.getElementById("stat-maxstreak"),
  };

  const game = {
    mode: "daily",
    pool: [],
    target: null, // { word, term }
    maxGuesses: 6,
    guesses: [], // [{ guess, result }]
    currentGuess: "",
    gameOver: false,
    win: false,
    keyStatus: {}, // letter -> 'correct' | 'present' | 'absent'
  };

  function utcDateStr(d) {
    return (d || new Date()).toISOString().slice(0, 10);
  }

  function hashString(str) {
    let h = 0;
    for (let i = 0; i < str.length; i++) {
      h = (h * 31 + str.charCodeAt(i)) >>> 0;
    }
    return h;
  }

  function maxGuessesFor(length) {
    if (length <= 5) return 6;
    if (length === 6) return 7;
    if (length === 7) return 8;
    return 9;
  }

  function buildPool(terms) {
    const seen = new Map();
    terms.forEach((t) => {
      let word = t.puzzleWord;
      if (!word && /^[A-Za-z]+$/.test(t.term) && t.term.length >= 4 && t.term.length <= 8) {
        word = t.term.toUpperCase();
      }
      if (!word) return;
      word = word.toUpperCase();
      if (!seen.has(word)) seen.set(word, t);
    });
    return Array.from(seen.entries()).map(([word, term]) => ({ word, term }));
  }

  function pickDaily(pool, dateStr) {
    const idx = hashString(dateStr) % pool.length;
    return pool[idx];
  }

  function pickRandom(pool, excludeWord) {
    let choice;
    do {
      choice = pool[Math.floor(Math.random() * pool.length)];
    } while (pool.length > 1 && choice.word === excludeWord);
    return choice;
  }

  function loadStats() {
    try {
      return (
        JSON.parse(localStorage.getItem(STATS_KEY)) || {
          played: 0,
          won: 0,
          currentStreak: 0,
          maxStreak: 0,
        }
      );
    } catch (e) {
      return { played: 0, won: 0, currentStreak: 0, maxStreak: 0 };
    }
  }

  function saveStats(stats) {
    try {
      localStorage.setItem(STATS_KEY, JSON.stringify(stats));
    } catch (e) {
      /* ignore */
    }
  }

  function renderStats() {
    const stats = loadStats();
    els.statPlayed.textContent = stats.played;
    els.statWinPct.textContent =
      stats.played > 0 ? Math.round((stats.won / stats.played) * 100) + "%" : "0%";
    els.statStreak.textContent = stats.currentStreak;
    els.statMaxStreak.textContent = stats.maxStreak;
  }

  function recordResult(win) {
    const stats = loadStats();
    stats.played += 1;
    if (win) {
      stats.won += 1;
      stats.currentStreak += 1;
      stats.maxStreak = Math.max(stats.maxStreak, stats.currentStreak);
    } else {
      stats.currentStreak = 0;
    }
    saveStats(stats);
    renderStats();
  }

  function saveProgress() {
    const key = game.mode === "daily" ? DAILY_KEY : PRACTICE_KEY;
    const payload = {
      date: utcDateStr(),
      word: game.target.word,
      slug: game.target.term.slug,
      guesses: game.guesses,
      gameOver: game.gameOver,
      win: game.win,
    };
    try {
      localStorage.setItem(key, JSON.stringify(payload));
    } catch (e) {
      /* ignore */
    }
  }

  function loadProgress(mode) {
    const key = mode === "daily" ? DAILY_KEY : PRACTICE_KEY;
    try {
      return JSON.parse(localStorage.getItem(key));
    } catch (e) {
      return null;
    }
  }

  function evaluateGuess(guess, target) {
    const result = new Array(guess.length).fill("absent");
    const used = new Array(target.length).fill(false);

    for (let i = 0; i < guess.length; i++) {
      if (guess[i] === target[i]) {
        result[i] = "correct";
        used[i] = true;
      }
    }
    for (let i = 0; i < guess.length; i++) {
      if (result[i] === "correct") continue;
      const idx = target.split("").findIndex((ch, j) => ch === guess[i] && !used[j]);
      if (idx !== -1) {
        result[i] = "present";
        used[idx] = true;
      }
    }
    return result;
  }

  function updateKeyStatus(guess, result) {
    const rank = { absent: 0, present: 1, correct: 2 };
    for (let i = 0; i < guess.length; i++) {
      const letter = guess[i];
      const newStatus = result[i];
      const existing = game.keyStatus[letter];
      if (!existing || rank[newStatus] > rank[existing]) {
        game.keyStatus[letter] = newStatus;
      }
    }
  }

  function startPuzzle(mode, forceNewPractice) {
    game.mode = mode;
    els.tabDaily.classList.toggle("active", mode === "daily");
    els.tabDaily.setAttribute("aria-selected", String(mode === "daily"));
    els.tabPractice.classList.toggle("active", mode === "practice");
    els.tabPractice.setAttribute("aria-selected", String(mode === "practice"));

    const today = utcDateStr();
    const saved = loadProgress(mode);

    let target;
    if (mode === "daily") {
      target = pickDaily(game.pool, today);
    } else if (saved && !forceNewPractice && saved.word) {
      target = game.pool.find((p) => p.word === saved.word) || pickRandom(game.pool);
    } else {
      const currentWord = game.target && game.mode === "practice" ? game.target.word : null;
      target = pickRandom(game.pool, currentWord);
    }

    game.target = target;
    game.maxGuesses = maxGuessesFor(target.word.length);
    game.guesses = [];
    game.currentGuess = "";
    game.gameOver = false;
    game.win = false;
    game.keyStatus = {};

    const canResume =
      saved &&
      saved.word === target.word &&
      (mode !== "daily" || saved.date === today);

    if (canResume) {
      game.guesses = saved.guesses || [];
      game.gameOver = saved.gameOver;
      game.win = saved.win;
      game.guesses.forEach((g) => updateKeyStatus(g.guess, g.result));
    }

    els.status.textContent = "";
    els.endPanel.hidden = true;
    els.practiceAgainBtn.hidden = mode !== "practice";

    renderBoard();
    renderKeyboard();
    renderStats();

    if (game.gameOver) {
      showEndPanel();
    }
  }

  function renderBoard() {
    const cols = game.target.word.length;
    els.board.style.setProperty("--cols", cols);
    els.board.style.setProperty("--rows", game.maxGuesses);
    els.board.innerHTML = "";

    for (let r = 0; r < game.maxGuesses; r++) {
      const row = document.createElement("div");
      row.className = "board-row";

      const submitted = game.guesses[r];
      const isCurrentRow = !submitted && r === game.guesses.length;
      const letters = submitted
        ? submitted.guess.split("")
        : isCurrentRow
        ? game.currentGuess.split("")
        : [];

      for (let c = 0; c < cols; c++) {
        const tile = document.createElement("div");
        tile.className = "tile";
        const letter = letters[c];
        if (letter) {
          tile.textContent = letter;
          tile.classList.add(submitted ? submitted.result[c] : "filled");
        }
        row.appendChild(tile);
      }
      els.board.appendChild(row);
    }
  }

  function renderKeyboard() {
    els.keyboard.innerHTML = "";
    KEYBOARD_ROWS.forEach((rowKeys) => {
      const row = document.createElement("div");
      row.className = "keyboard-row";
      rowKeys.forEach((key) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "key";
        if (key === "ENTER" || key === "BACK") btn.classList.add("wide");
        btn.textContent = key === "BACK" ? "⌫" : key === "ENTER" ? "Enter" : key;
        const status = game.keyStatus[key];
        if (status) btn.classList.add(status);
        btn.addEventListener("click", () => handleKey(key));
        row.appendChild(btn);
      });
      els.keyboard.appendChild(row);
    });
  }

  function flashStatus(msg) {
    els.status.textContent = msg;
  }

  function shakeCurrentRow() {
    const rowEl = els.board.children[game.guesses.length];
    if (!rowEl) return;
    rowEl.querySelectorAll(".tile").forEach((t) => {
      t.classList.add("shake");
      t.addEventListener("animationend", () => t.classList.remove("shake"), { once: true });
    });
  }

  function submitGuess() {
    const target = game.target.word;
    if (game.currentGuess.length !== target.length) {
      flashStatus("Not enough letters");
      shakeCurrentRow();
      return;
    }
    const guess = game.currentGuess;
    const result = evaluateGuess(guess, target);
    game.guesses.push({ guess, result });
    updateKeyStatus(guess, result);
    game.currentGuess = "";

    const won = result.every((r) => r === "correct");
    if (won) {
      game.gameOver = true;
      game.win = true;
      flashStatus("");
    } else if (game.guesses.length >= game.maxGuesses) {
      game.gameOver = true;
      game.win = false;
      flashStatus("");
    } else {
      flashStatus("");
    }

    saveProgress();
    renderBoard();
    renderKeyboard();

    if (game.gameOver) {
      if (game.mode === "daily") recordResult(game.win);
      showEndPanel();
    }
  }

  function handleKey(key) {
    if (game.gameOver) return;
    if (key === "ENTER") {
      submitGuess();
    } else if (key === "BACK" || key === "BACKSPACE") {
      game.currentGuess = game.currentGuess.slice(0, -1);
      renderBoard();
    } else if (/^[A-Z]$/.test(key) && game.currentGuess.length < game.target.word.length) {
      game.currentGuess += key;
      renderBoard();
    }
  }

  function showEndPanel() {
    const term = game.target.term;
    els.endTitle.textContent = game.win
      ? "You got it! 🎉 — " + term.term
      : "So close — it was " + term.term;
    els.endDef.textContent = term.definition;
    els.endExample.textContent = "“" + term.example.replace(/^["“]+|["”]+$/g, "") + "”";
    els.endOrigin.textContent = term.origin;
    els.viewLink.href = "index.html#" + term.slug;
    els.endPanel.hidden = false;
    els.practiceAgainBtn.hidden = game.mode !== "practice";
    els.endPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function buildShareText() {
    const rows = game.guesses
      .map((g) =>
        g.result
          .map((r) => (r === "correct" ? "🟩" : r === "present" ? "🟨" : "⬛"))
          .join("")
      )
      .join("\n");
    const label =
      game.mode === "daily"
        ? "Torontle " + utcDateStr()
        : "Torontle (Practice)";
    const scoreLine = game.win
      ? game.guesses.length + "/" + game.maxGuesses
      : "X/" + game.maxGuesses;
    return label + " " + scoreLine + "\n\n" + rows;
  }

  function shareResult() {
    const text = buildShareText();
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard
        .writeText(text)
        .then(() => flashStatus("Copied to clipboard!"))
        .catch(() => promptFallbackShare(text));
    } else {
      promptFallbackShare(text);
    }
  }

  function promptFallbackShare(text) {
    window.prompt("Copy your result:", text);
  }

  function init() {
    fetch("data/terms.json")
      .then((res) => res.json())
      .then((terms) => {
        game.pool = buildPool(terms);
        startPuzzle("daily");
      })
      .catch((err) => {
        els.status.textContent =
          "Couldn't load word data. If you opened this file directly, run a local server (see README).";
        console.error(err);
      });

    document.addEventListener("keydown", (e) => {
      if (els.endPanel && !els.endPanel.hidden && document.activeElement.tagName === "INPUT") return;
      const key = e.key.toUpperCase();
      if (key === "ENTER") handleKey("ENTER");
      else if (key === "BACKSPACE") handleKey("BACK");
      else if (/^[A-Z]$/.test(key)) handleKey(key);
    });

    els.tabDaily.addEventListener("click", () => startPuzzle("daily"));
    els.tabPractice.addEventListener("click", () => startPuzzle("practice"));
    els.practiceAgainBtn.addEventListener("click", () => startPuzzle("practice", true));
    els.shareBtn.addEventListener("click", shareResult);
  }

  document.addEventListener("DOMContentLoaded", init);
})();
