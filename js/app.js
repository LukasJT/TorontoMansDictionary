// Toronto Mans Dictionary — vanilla JS, no build step, no framework.
// Loads data/terms.json and renders a searchable/filterable dictionary.

(function () {
  "use strict";

  const state = {
    terms: [],
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
    template: document.getElementById("term-card-template"),
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

  function fetchTerms() {
    return fetch("data/terms.json")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to load terms.json");
        return res.json();
      });
  }

  function uniqueCategories(terms) {
    const set = new Set();
    terms.forEach((t) => (t.categories || []).forEach((c) => set.add(c)));
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

  function matchesQuery(term, q) {
    if (!q) return true;
    const hay = (term.term + " " + term.definition + " " + term.example).toLowerCase();
    return hay.includes(q);
  }

  function matchesCategory(term, cat) {
    if (cat === "All") return true;
    return (term.categories || []).includes(cat);
  }

  function getFiltered() {
    const q = state.query.trim().toLowerCase();
    let list = state.terms.filter(
      (t) => matchesQuery(t, q) && matchesCategory(t, state.category)
    );
    if (state.sort === "az") {
      list = list.slice().sort((a, b) => a.term.localeCompare(b.term));
    } else if (state.sort === "za") {
      list = list.slice().sort((a, b) => b.term.localeCompare(a.term));
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

  function stripQuotes(str) {
    return str.replace(/^["“]+|["”]+$/g, "");
  }

  function buildCard(term) {
    const node = els.template.content.firstElementChild.cloneNode(true);
    const header = node.querySelector(".term-card-header");
    const body = node.querySelector(".term-body");

    node.dataset.slug = term.slug;
    node.querySelector(".term-name").textContent = term.term;
    node.querySelector(".term-cats").textContent = (term.categories || [])[0] || "";
    node.querySelector(".term-definition").textContent = term.definition;
    node.querySelector(".term-example").textContent = "“" + stripQuotes(term.example) + "”";
    node.querySelector(".term-origin").textContent = term.origin;

    header.addEventListener("click", () => {
      const expanded = header.getAttribute("aria-expanded") === "true";
      header.setAttribute("aria-expanded", String(!expanded));
      body.hidden = expanded;
    });

    wireVotes(node, term);

    return node;
  }

  function wireVotes(node, term) {
    const votes = loadVotes();
    const base = baseVoteCounts(term.slug);
    const record = votes[term.slug] || { dir: 0 };

    const upBtn = node.querySelector(".vote-up");
    const downBtn = node.querySelector(".vote-down");
    const upCount = node.querySelector(".vote-up-count");
    const downCount = node.querySelector(".vote-down-count");

    function paint() {
      upCount.textContent = base.up + (record.dir === 1 ? 1 : 0);
      downCount.textContent = base.down + (record.dir === -1 ? 1 : 0);
      upBtn.classList.toggle("voted-up", record.dir === 1);
      downBtn.classList.toggle("voted-down", record.dir === -1);
    }

    function vote(dir) {
      record.dir = record.dir === dir ? 0 : dir;
      votes[term.slug] = record;
      saveVotes(votes);
      paint();
    }

    upBtn.addEventListener("click", () => vote(1));
    downBtn.addEventListener("click", () => vote(-1));
    paint();
  }

  function render() {
    const list = getFiltered();
    els.grid.innerHTML = "";
    const frag = document.createDocumentFragment();
    list.forEach((term) => frag.appendChild(buildCard(term)));
    els.grid.appendChild(frag);

    els.noResults.hidden = list.length !== 0;
    els.grid.hidden = list.length === 0;

    const total = state.terms.length;
    if (state.query.trim() || state.category !== "All") {
      els.resultsMeta.textContent = `${list.length} of ${total} terms match`;
    } else {
      els.resultsMeta.textContent = `${total} terms and counting`;
    }
  }

  function renderWordOfTheDay() {
    if (!state.terms.length) return;
    const idx = dayIndex() % state.terms.length;
    const term = state.terms[idx];
    els.wotdCard.innerHTML = "";
    const h3 = document.createElement("h3");
    h3.textContent = term.term;
    const def = document.createElement("p");
    def.className = "term-definition";
    def.textContent = term.definition;
    const ex = document.createElement("p");
    ex.className = "term-example";
    ex.textContent = "“" + stripQuotes(term.example) + "”";
    const origin = document.createElement("p");
    origin.className = "term-origin";
    origin.textContent = term.origin;
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

  function init() {
    fetchTerms()
      .then((terms) => {
        state.terms = terms;
        els.heroCount.textContent = `${terms.length} words defined so far`;
        renderChips(uniqueCategories(terms));
        renderWordOfTheDay();
        render();
        openTermFromHash();
      })
      .catch((err) => {
        els.grid.innerHTML = "";
        els.noResults.hidden = false;
        els.noResults.textContent =
          "Couldn't load the dictionary data. If you opened this file directly, run a local server (see README) — browsers block fetch() on file:// URLs.";
        console.error(err);
      });

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
      renderChips(uniqueCategories(state.terms));
      render();
    });

    els.sortSelect.addEventListener("change", () => {
      state.sort = els.sortSelect.value;
      render();
    });

    els.randomBtn.addEventListener("click", () => {
      if (!state.terms.length) return;
      const term = state.terms[Math.floor(Math.random() * state.terms.length)];
      state.query = term.term;
      els.searchInput.value = term.term;
      state.category = "All";
      renderChips(uniqueCategories(state.terms));
      render();
      document.getElementById("browse").scrollIntoView({ behavior: "smooth" });
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
