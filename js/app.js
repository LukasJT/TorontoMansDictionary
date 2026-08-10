// Toronto Mans Dictionary — vanilla JS, no build step, no framework.
// Term cards are pre-rendered static HTML (see scripts/build.py) so search
// engines and no-JS visitors get the real content. This file enhances that
// existing markup in place — filtering/sorting/reordering DOM nodes rather
// than building them from a fetch() — plus word-of-the-day and voting.

(function () {
  "use strict";

  const state = {
    order: [], // stable original DOM order (master list, used for word-of-the-day / random)
    query: "",
    category: "All",
    sort: "az",
  };

  const els = {
    grid: document.getElementById("term-grid"),
    noResults: document.getElementById("no-results"),
    resultsMeta: document.getElementById("results-meta"),
    chips: document.getElementById("category-chips"),
    sortSelect: document.getElementById("sort-select"),
    searchForm: document.getElementById("search-form"),
    searchInput: document.getElementById("search-input"),
    clearSearchLink: document.getElementById("clear-search-link"),
    randomBtn: document.getElementById("random-btn"),
    heroCount: document.getElementById("hero-count"),
    wotdCard: document.getElementById("wotd-card"),
  };

  const VOTES_KEY = "tmd-votes-v1";

  function loadVotes() {
    try {
      return JSON.parse(localStorage.getItem(VOTES_KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function saveVotes(votes) {
    try {
      localStorage.setItem(VOTES_KEY, JSON.stringify(votes));
    } catch (e) {
      /* localStorage unavailable — votes just won't persist */
    }
  }

  function baseVoteCounts(slug) {
    // Deterministic pseudo-random seed so counts feel alive but are stable per term.
    let hash = 0;
    for (let i = 0; i < slug.length; i++) {
      hash = (hash * 31 + slug.charCodeAt(i)) >>> 0;
    }
    const up = 40 + (hash % 260);
    const down = 3 + (hash % 17);
    return { up, down };
  }

  function dayIndex() {
    const start = new Date(Date.UTC(2026, 0, 1));
    const now = new Date();
    const diffDays = Math.floor((now - start) / 86400000);
    return diffDays;
  }

  function cardData(card) {
    return {
      slug: card.dataset.slug,
      term: card.querySelector(".term-name").textContent,
      categories: (card.dataset.categories || "").split("|").filter(Boolean),
      definition: card.querySelector(".term-definition").textContent,
      example: card.querySelector(".term-example").textContent,
      origin: card.querySelector(".term-origin").textContent,
    };
  }

  function uniqueCategories(cards) {
    const set = new Set();
    cards.forEach((c) => (c.dataset.categories || "").split("|").filter(Boolean).forEach((cat) => set.add(cat)));
    return Array.from(set).sort();
  }

  function renderChips(categories) {
    els.chips.innerHTML = "";
    const all = ["All", ...categories];
    all.forEach((cat) => {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "chip" + (cat === state.category ? " active" : "");
      chip.textContent = cat;
      chip.addEventListener("click", () => {
        state.category = cat;
        renderChips(categories);
        render();
      });
      els.chips.appendChild(chip);
    });
  }

  function matchesQuery(card, q) {
    if (!q) return true;
    const hay = card.textContent.toLowerCase();
    return hay.includes(q);
  }

  function matchesCategory(card, cat) {
    if (cat === "All") return true;
    return (card.dataset.categories || "").split("|").includes(cat);
  }

  function getFiltered() {
    const q = state.query.trim().toLowerCase();
    let list = state.order.filter(
      (card) => matchesQuery(card, q) && matchesCategory(card, state.category)
    );
    if (state.sort === "az") {
      list = list
        .slice()
        .sort((a, b) => a.querySelector(".term-name").textContent.localeCompare(b.querySelector(".term-name").textContent));
    } else if (state.sort === "za") {
      list = list
        .slice()
        .sort((a, b) => b.querySelector(".term-name").textContent.localeCompare(a.querySelector(".term-name").textContent));
    } else if (state.sort === "shuffle") {
      list = shuffledCopy(list);
    }
    return list;
  }

  function shuffledCopy(arr) {
    const copy = arr.slice();
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  function wireVotes(card) {
    const slug = card.dataset.slug;
    const votes = loadVotes();
    const base = baseVoteCounts(slug);
    const record = votes[slug] || { dir: 0 };

    const upBtn = card.querySelector(".vote-up");
    const downBtn = card.querySelector(".vote-down");
    const upCount = card.querySelector(".vote-up-count");
    const downCount = card.querySelector(".vote-down-count");

    function paint() {
      upCount.textContent = base.up + (record.dir === 1 ? 1 : 0);
      downCount.textContent = base.down + (record.dir === -1 ? 1 : 0);
      upBtn.classList.toggle("voted-up", record.dir === 1);
      downBtn.classList.toggle("voted-down", record.dir === -1);
    }

    function vote(dir) {
      record.dir = record.dir === dir ? 0 : dir;
      votes[slug] = record;
      saveVotes(votes);
      paint();
    }

    upBtn.addEventListener("click", () => vote(1));
    downBtn.addEventListener("click", () => vote(-1));
    paint();
  }

  function wireExpand(card) {
    const header = card.querySelector(".term-card-header");
    const body = card.querySelector(".term-body");
    header.addEventListener("click", () => {
      const expanded = header.getAttribute("aria-expanded") === "true";
      header.setAttribute("aria-expanded", String(!expanded));
      body.hidden = expanded;
    });
  }

  function render() {
    const list = getFiltered();
    const visible = new Set(list);

    // Reorder within the grid to match sort, then show/hide by filter match.
    list.forEach((card) => els.grid.appendChild(card));
    state.order.forEach((card) => {
      card.hidden = !visible.has(card);
    });

    els.noResults.hidden = list.length !== 0;

    const total = state.order.length;
    if (state.query.trim() || state.category !== "All") {
      els.resultsMeta.textContent = `${list.length} of ${total} terms match`;
    } else {
      els.resultsMeta.textContent = `${total} terms and counting`;
    }
  }

  function renderWordOfTheDay() {
    if (!state.order.length) return;
    const idx = dayIndex() % state.order.length;
    const data = cardData(state.order[idx]);
    els.wotdCard.innerHTML = "";
    const h3 = document.createElement("h3");
    h3.textContent = data.term;
    const def = document.createElement("p");
    def.className = "term-definition";
    def.textContent = data.definition;
    const ex = document.createElement("p");
    ex.className = "term-example";
    ex.textContent = data.example;
    const origin = document.createElement("p");
    origin.className = "term-origin";
    origin.textContent = data.origin;
    els.wotdCard.append(h3, def, ex, origin);
  }

  function openTermFromHash() {
    const slug = location.hash.replace(/^#/, "");
    if (!slug) return;
    const card = els.grid.querySelector('[data-slug="' + CSS.escape(slug) + '"]');
    if (!card) return;
    const header = card.querySelector(".term-card-header");
    const body = card.querySelector(".term-body");
    header.setAttribute("aria-expanded", "true");
    body.hidden = false;
    card.scrollIntoView({ behavior: "smooth", block: "center" });
    card.classList.add("term-card-highlight");
  }

  function applyQueryParam(categories) {
    const params = new URLSearchParams(location.search);
    const q = params.get("q");
    if (q) {
      state.query = q;
      els.searchInput.value = q;
    }
    const cat = params.get("cat");
    if (cat && categories.includes(cat)) {
      state.category = cat;
    }
  }

  function init() {
    const cards = Array.from(els.grid.querySelectorAll(".term-card"));
    if (!cards.length) return;

    state.order = cards;
    cards.forEach((card) => {
      wireExpand(card);
      wireVotes(card);
    });

    const categories = uniqueCategories(cards);
    els.heroCount.textContent = `${cards.length} words defined so far`;
    renderWordOfTheDay();
    applyQueryParam(categories);
    renderChips(categories);
    render();
    openTermFromHash();
    if (new URLSearchParams(location.search).get("cat")) {
      document.getElementById("browse").scrollIntoView();
    }

    els.searchForm.addEventListener("submit", (e) => {
      e.preventDefault();
      state.query = els.searchInput.value;
      render();
      document.getElementById("browse").scrollIntoView({ behavior: "smooth" });
    });

    els.searchInput.addEventListener("input", () => {
      state.query = els.searchInput.value;
      render();
    });

    els.clearSearchLink.addEventListener("click", (e) => {
      e.preventDefault();
      state.query = "";
      els.searchInput.value = "";
      state.category = "All";
      renderChips(uniqueCategories(state.order));
      render();
    });

    els.sortSelect.addEventListener("change", () => {
      state.sort = els.sortSelect.value;
      render();
    });

    els.randomBtn.addEventListener("click", () => {
      if (!state.order.length) return;
      const card = state.order[Math.floor(Math.random() * state.order.length)];
      state.query = card.querySelector(".term-name").textContent;
      els.searchInput.value = state.query;
      state.category = "All";
      renderChips(uniqueCategories(state.order));
      render();
      document.getElementById("browse").scrollIntoView({ behavior: "smooth" });
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
