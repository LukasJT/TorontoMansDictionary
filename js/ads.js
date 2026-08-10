// Ad support: fills the small "house ad" tiles beside/inside ad units with
// promos for our other sites, and swaps a house ad into any ad unit the
// network doesn't fill (detected by checking whether the network's script
// actually wrote an iframe into the container within a few seconds).
//
// House-ad copy below is a minimal, honest guess at what each site is based
// only on its domain name — nothing here is a verified feature claim.

(function () {
  "use strict";

  const HOUSE_SITES = [
    { url: "https://tornadosimulator.net", name: "TornadoSimulator.net", tagline: "Simulate tornado formation and behaviour." },
    { url: "https://vitamindcalculator.net", name: "VitaminDCalculator.net", tagline: "Calculate your recommended vitamin D intake." },
    { url: "https://celestialvisibility.com", name: "CelestialVisibility.com", tagline: "See what's visible in the night sky tonight." },
    { url: "https://123videos.net", name: "123Videos.net", tagline: "Watch and share videos." },
    { url: "https://homelesshelp.net", name: "HomelessHelp.net", tagline: "Resources and support for homelessness." },
  ];

  function randomSite() {
    return HOUSE_SITES[Math.floor(Math.random() * HOUSE_SITES.length)];
  }

  function houseAdCard() {
    const site = randomSite();
    const a = document.createElement("a");
    a.className = "house-ad-card";
    a.href = site.url;
    a.target = "_blank";
    a.rel = "noopener sponsored";
    a.innerHTML =
      '<span class="house-ad-kicker">Also by us</span>' +
      '<span class="house-ad-name">' + site.name + "</span>" +
      '<span class="house-ad-tagline">' + site.tagline + "</span>";
    return a;
  }

  function fillHouseAdSlots() {
    document.querySelectorAll(".house-ad-slot").forEach((slot) => {
      if (slot.childElementCount === 0) {
        slot.appendChild(houseAdCard());
      }
    });
  }

  function fallbackUnfilledAdUnits() {
    document.querySelectorAll(".ad-unit[data-ad]").forEach((unit) => {
      if (!unit.querySelector("iframe")) {
        unit.innerHTML = "";
        const wrap = document.createElement("div");
        wrap.className = "ad-fallback";
        wrap.appendChild(houseAdCard());
        unit.appendChild(wrap);
      }
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    fillHouseAdSlots();
    // Give the ad network's script time to load and render before deciding
    // it didn't fill — most invoke.js-style tags render within ~1-2s.
    window.setTimeout(fallbackUnfilledAdUnits, 2200);
  });
})();
