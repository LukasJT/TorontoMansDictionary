// Toronto Trivia Quiz — general-knowledge questions pulled from the Toronto
// Guide section (history, geography, sports, infrastructure, culture), as
// opposed to js/quiz.js which tests slang definitions specifically.
// Question bank is hardcoded here rather than fetched, since guide content
// isn't structured data like data/terms.json.

(function () {
  "use strict";

  const QUESTIONS = [
    {
      q: 'What was Toronto called before it was incorporated as a city in 1834?',
      options: ['York', 'Hogtown', 'Upper Canada', 'Fort Rouillé'],
      correct: 0,
      link: { href: '../guide/history.html', label: 'The History of Toronto' },
    },
    {
      q: 'The modern City of Toronto was formed in 1998 by merging how many separate municipalities?',
      options: ['Three', 'Four', 'Five', 'Six'],
      correct: 3,
      link: { href: '../guide/history.html', label: 'The History of Toronto' },
    },
    {
      q: 'Roughly what does "Tkaronto," the Mohawk word behind Toronto’s name, mean?',
      options: [
        'Meeting place of nations',
        'Where there are trees standing in the water',
        'Land beside the great lake',
        'City of the north wind',
      ],
      correct: 1,
      link: { href: '../guide/indigenous-history.html', label: "Toronto's Indigenous History" },
    },
    {
      q: 'Who co-discovered insulin at the University of Toronto in 1921?',
      options: ['Alexander Graham Bell', 'Frederick Banting', 'Sandford Fleming', 'John Kenneth Galbraith'],
      correct: 1,
      link: { href: '../guide/medical-history.html', label: "Toronto's Medical History" },
    },
    {
      q: 'The CN Tower held which world record from 1975 until Dubai’s Burj Khalifa passed it in 2007?',
      options: [
        'Tallest freestanding structure on Earth',
        'Tallest occupied building',
        'Largest revolving restaurant',
        'Fastest elevator',
      ],
      correct: 0,
      link: { href: '../guide/cn-tower.html', label: 'The CN Tower' },
    },
    {
      q: 'Which GTA city is home to Canada’s Wonderland?',
      options: ['Markham', 'Brampton', 'Vaughan', 'Richmond Hill'],
      correct: 2,
      link: { href: '../guide/vaughan.html', label: 'Vaughan' },
    },
    {
      q: 'Toronto’s old nickname "Hogtown" comes from what 19th-century industry?',
      options: ['Shipbuilding', 'Meatpacking', 'Textiles', 'Brewing'],
      correct: 1,
      link: { href: '../guide/nicknames.html', label: 'Every Toronto Nickname, Explained' },
    },
    {
      q: 'What year did Toronto’s subway — Canada’s first — open?',
      options: ['1948', '1954', '1963', '1971'],
      correct: 1,
      link: { href: '../guide/transit.html', label: 'Toronto Transit' },
    },
    {
      q: 'Which team did the Blue Jays beat to win their second straight World Series in 1993?',
      options: ['Atlanta Braves', 'Philadelphia Phillies', 'New York Yankees', 'Los Angeles Dodgers'],
      correct: 1,
      link: { href: '../guide/blue-jays-1992.html', label: "The Blue Jays' Back-to-Back World Series" },
    },
    {
      q: 'What year did the Toronto Maple Leafs last win the Stanley Cup?',
      options: ['1951', '1962', '1967', '1993'],
      correct: 2,
      link: { href: '../guide/maple-leafs-1967.html', label: "1967: The Maple Leafs' Last Stanley Cup" },
    },
    {
      q: 'Who hit the historic Game 7 buzzer-beater that sent the Raptors to the 2019 Eastern Conference Finals?',
      options: ['Kyle Lowry', 'Pascal Siakam', 'Kawhi Leonard', 'DeMar DeRozan'],
      correct: 2,
      link: { href: '../guide/raptors-2019.html', label: 'The 2019 Toronto Raptors' },
    },
    {
      q: 'What is the PATH?',
      options: [
        'A downtown bike lane network',
        'The world’s largest underground pedestrian network',
        'A GO Transit rail line',
        'A hiking trail along the waterfront',
      ],
      correct: 1,
      link: { href: '../guide/path.html', label: 'The PATH' },
    },
    {
      q: 'Which Toronto neighbourhood banned the sale of alcohol from 1904 until 1998?',
      options: ['Cabbagetown', 'The Junction', 'Corktown', 'Riverdale'],
      correct: 1,
      link: { href: '../guide/the-junction.html', label: 'The Junction' },
    },
    {
      q: 'The Bloor (Prince Edward) Viaduct was built in 1918 with a lower deck for a subway line that didn’t open until:',
      options: ['1930', '1954', '1966', '1980'],
      correct: 2,
      link: { href: '../guide/bloor-viaduct.html', label: 'The Bloor Viaduct' },
    },
    {
      q: 'What does Toronto slang call Mississauga?',
      options: ['The Dot', 'Sauga', 'T.O.', 'The Hammer'],
      correct: 1,
      link: { href: '../guide/mississauga.html', label: 'Mississauga' },
    },
    {
      q: 'Toronto’s main water filtration plant is nicknamed the:',
      options: ['Palace of Purification', 'Crystal Fortress', 'Hall of Waters', 'Great Reservoir'],
      correct: 0,
      link: { href: '../guide/water-treatment.html', label: 'The R.C. Harris Water Treatment Plant' },
    },
    {
      q: 'Rogers Centre (originally SkyDome) made history in 1989 as the world’s first stadium with:',
      options: [
        'Artificial turf',
        'A Jumbotron screen',
        'A fully retractable roof',
        'Instant replay technology',
      ],
      correct: 2,
      link: { href: '../guide/rogers-centre.html', label: 'Rogers Centre (SkyDome)' },
    },
    {
      q: 'Hurricane Hazel, Toronto’s deadliest storm, hit the city in what year?',
      options: ['1929', '1954', '1972', '1998'],
      correct: 1,
      link: { href: '../guide/extreme-weather.html', label: "Toronto's Worst Storms" },
    },
    {
      q: 'Which is Canada’s oldest school dedicated to art and design, founded in Toronto in 1876?',
      options: ['OCAD University', 'York University', 'Ryerson Institute', 'Central Technical School'],
      correct: 0,
      link: { href: '../guide/ocad-university.html', label: 'OCAD University' },
    },
    {
      q: 'The Royal Ontario Museum’s controversial 2007 glass-and-metal addition is called the:',
      options: ['Prism', 'Crystal', 'Diamond Wing', 'Lantern'],
      correct: 1,
      link: { href: '../guide/rom.html', label: 'The Royal Ontario Museum' },
    },
    {
      q: 'Which government body has controlled alcohol retail in Ontario since 1927?',
      options: ['LCBO', 'AGCO', 'OLG', 'Beer Store Corp.'],
      correct: 0,
      link: { href: '../guide/lcbo-history.html', label: 'The LCBO' },
    },
    {
      q: 'The Group of Seven, Canada’s most famous school of landscape painters, first exhibited together in Toronto in what year?',
      options: ['1900', '1920', '1945', '1967'],
      correct: 1,
      link: { href: '../guide/group-of-seven.html', label: 'The Group of Seven' },
    },
    {
      q: 'Which Toronto suburb was built around Canada’s largest flower-growing business and is still nicknamed "the Flower City"?',
      options: ['Brampton', 'Oakville', 'Newmarket', 'Whitby'],
      correct: 0,
      link: { href: '../guide/brampton.html', label: 'Brampton' },
    },
    {
      q: 'Which Ontario town is named after a British warship that fought in the 1939 Battle of the River Plate?',
      options: ['Ajax', 'Whitby', 'Pickering', 'Milton'],
      correct: 0,
      link: { href: '../guide/ajax.html', label: 'Ajax' },
    },
  ];

  const els = {
    start: document.getElementById('quiz-start'),
    startBtn: document.getElementById('quiz-start-btn'),
    play: document.getElementById('quiz-play'),
    progress: document.getElementById('quiz-progress'),
    question: document.getElementById('quiz-question'),
    options: document.getElementById('quiz-options'),
    result: document.getElementById('quiz-result'),
    resultTitle: document.getElementById('quiz-result-title'),
    resultSub: document.getElementById('quiz-result-sub'),
    resultLinks: document.getElementById('quiz-result-links'),
    againBtn: document.getElementById('quiz-again-btn'),
  };

  const ROUND_SIZE = 12;
  let round = [];
  let index = 0;
  let score = 0;
  let answered = false;
  let missed = [];

  function shuffledCopy(arr) {
    const copy = arr.slice();
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  function showPanel(panel) {
    [els.start, els.play, els.result].forEach((p) => (p.hidden = p !== panel));
  }

  function renderQuestion() {
    answered = false;
    const q = round[index];
    els.progress.textContent = `Question ${index + 1} of ${round.length} — score: ${score}`;
    els.question.textContent = q.q;
    els.options.innerHTML = '';
    q.options.forEach((opt, i) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'quiz-option';
      btn.textContent = opt;
      btn.addEventListener('click', () => selectAnswer(btn, i, q));
      els.options.appendChild(btn);
    });
  }

  function selectAnswer(btn, chosenIndex, q) {
    if (answered) return;
    answered = true;
    const correct = chosenIndex === q.correct;
    if (correct) {
      score++;
    } else {
      missed.push(q);
    }

    Array.from(els.options.children).forEach((b) => {
      b.disabled = true;
    });
    btn.classList.add(correct ? 'quiz-option-correct' : 'quiz-option-wrong');
    if (!correct) {
      els.options.children[q.correct].classList.add('quiz-option-correct');
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
    if (pct === 100) verdict = 'Perfect score — you know this city cold. 🍁';
    else if (pct >= 80) verdict = "You've clearly read the whole guide.";
    else if (pct >= 50) verdict = 'Solid, but there’s more of the city to explore.';
    else verdict = 'Time to dig into the Toronto Guide.';

    els.resultTitle.textContent = `${score} / ${round.length} — ${pct}%`;
    els.resultSub.textContent = verdict;

    els.resultLinks.innerHTML = '';
    if (missed.length) {
      const heading = document.createElement('p');
      heading.className = 'quiz-missed-heading';
      heading.textContent = 'Brush up on what you missed:';
      els.resultLinks.appendChild(heading);
      const seen = new Set();
      missed.slice(0, 5).forEach((m) => {
        if (seen.has(m.link.href)) return;
        seen.add(m.link.href);
        const a = document.createElement('a');
        a.className = 'chip-static';
        a.href = m.link.href;
        a.textContent = m.link.label;
        els.resultLinks.appendChild(a);
      });
    }

    showPanel(els.result);
  }

  function startRound() {
    round = shuffledCopy(QUESTIONS)
      .slice(0, ROUND_SIZE)
      .map((q) => {
        const opts = q.options.map((text, i) => ({ text, isCorrect: i === q.correct }));
        const shuffled = shuffledCopy(opts);
        return {
          q: q.q,
          link: q.link,
          options: shuffled.map((o) => o.text),
          correct: shuffled.findIndex((o) => o.isCorrect),
        };
      });
    index = 0;
    score = 0;
    missed = [];
    showPanel(els.play);
    renderQuestion();
  }

  function init() {
    els.startBtn.disabled = false;
    els.startBtn.textContent = 'Start the quiz →';
    els.startBtn.addEventListener('click', startRound);
    els.againBtn.addEventListener('click', startRound);
  }

  document.addEventListener('DOMContentLoaded', init);
})();
