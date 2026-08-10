// Toronto Slang Quiz — 10 multiple-choice questions built from this site's
// own dictionary data. Correct answer is the real definition; the three
// distractors are other terms' real definitions, shuffled in. No backend,
// no stored scores.

(function () {
  "use strict";

  const QUESTION_COUNT = 10;
  const OPTION_COUNT = 4;

  const els = {
    start: document.getElementById("quiz-start"),
    startBtn: document.getElementById("quiz-start-btn"),
    play: document.getElementById("quiz-play"),
    progress: document.getElementById("quiz-progress"),
    question: document.getElementById("quiz-question"),
    options: document.getElementById("quiz-options"),
    result: document.getElementById("quiz-result"),
    resultTitle: document.getElementById("quiz-result-title"),
    resultSub: document.getElementById("quiz-result-sub"),
    againBtn: document.getElementById("quiz-again-btn"),
  };

  let allTerms = [];
  let round = [];
  let index = 0;
  let score = 0;
  let answered = false;

  function shuffledCopy(arr) {
    const copy = arr.slice();
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  function buildRound() {
    const pool = shuffledCopy(allTerms).slice(0, QUESTION_COUNT);
    return pool.map((term) => {
      const distractors = shuffledCopy(
        allTerms.filter((t) => t.slug !== term.slug)
      ).slice(0, OPTION_COUNT - 1);
      const options = shuffledCopy([term, ...distractors]);
      return { term, options };
    });
  }

  function showPanel(panel) {
    [els.start, els.play, els.result].forEach((p) => (p.hidden = p !== panel));
  }

  function renderQuestion() {
    answered = false;
    const q = round[index];
    els.progress.textContent = `Question ${index + 1} of ${round.length} — score: ${score}`;
    els.question.textContent = `What does "${q.term.term}" mean?`;
    els.options.innerHTML = "";
    q.options.forEach((opt) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "quiz-option";
      btn.textContent = opt.definition;
      btn.addEventListener("click", () => selectAnswer(btn, opt, q.term));
      els.options.appendChild(btn);
    });
  }

  function selectAnswer(btn, chosen, correctTerm) {
    if (answered) return;
    answered = true;
    const correct = chosen.slug === correctTerm.slug;
    if (correct) score++;

    Array.from(els.options.children).forEach((b) => {
      b.disabled = true;
    });
    btn.classList.add(correct ? "quiz-option-correct" : "quiz-option-wrong");
    if (!correct) {
      const correctBtn = Array.from(els.options.children).find(
        (b) => b.textContent === correctTerm.definition
      );
      if (correctBtn) correctBtn.classList.add("quiz-option-correct");
    }

    window.setTimeout(() => {
      index++;
      if (index < round.length) {
        renderQuestion();
      } else {
        showResult();
      }
    }, 1100);
  }

  function showResult() {
    const pct = Math.round((score / round.length) * 100);
    let verdict;
    if (pct === 100) verdict = "Certified Toronto mans. 🍁";
    else if (pct >= 80) verdict = "You clearly didn't just move here.";
    else if (pct >= 50) verdict = "Solid, but you've got some catching up to do.";
    else verdict = "Time to read the dictionary front to back.";

    els.resultTitle.textContent = `${score} / ${round.length} — ${pct}%`;
    els.resultSub.textContent = verdict;
    showPanel(els.result);
  }

  function startRound() {
    round = buildRound();
    index = 0;
    score = 0;
    showPanel(els.play);
    renderQuestion();
  }

  function init() {
    fetch("data/terms.json")
      .then((res) => res.json())
      .then((terms) => {
        allTerms = terms.filter((t) => t.definition && t.term);
        els.startBtn.disabled = false;
        els.startBtn.textContent = "Start the quiz →";
      })
      .catch((err) => {
        els.start.querySelector("p").textContent =
          "Couldn't load quiz data. If you opened this file directly, run a local server (see README).";
        console.error(err);
      });

    els.startBtn.addEventListener("click", startRound);
    els.againBtn.addEventListener("click", startRound);
  }

  document.addEventListener("DOMContentLoaded", init);
})();
