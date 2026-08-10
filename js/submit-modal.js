// Submit-a-term modal, shared across pages.
// No backend: builds a mailto: link to the site owner and hands off to the
// visitor's own email client. That's the only way a static site can move
// mail without a server or a third-party form service — the fallback box
// below covers people without a configured mail client.

(function () {
  "use strict";

  const RECIPIENT = "uppercanadadigital2026@gmail.com";

  function buildModal() {
    const overlay = document.createElement("div");
    overlay.className = "modal-overlay";
    overlay.id = "submit-modal-overlay";
    overlay.hidden = true;
    overlay.innerHTML =
      '<div class="modal" role="dialog" aria-modal="true" aria-labelledby="submit-modal-title">' +
        '<div class="modal-inner">' +
          '<button type="button" class="modal-close" id="submit-modal-close" aria-label="Close">&times;</button>' +
          '<h2 id="submit-modal-title">Submit a term</h2>' +
          '<p class="modal-sub">Fill this in and it opens an email to the site owner with everything filled out — hit send there to finish.</p>' +
          '<form id="submit-term-form">' +
            '<label for="st-term">Term / title</label>' +
            '<input id="st-term" name="term" type="text" required placeholder="e.g. Peak">' +

            '<label for="st-definition">Definition</label>' +
            '<textarea id="st-definition" name="definition" required placeholder="What does it mean?"></textarea>' +

            '<label for="st-example">Example (optional)</label>' +
            '<input id="st-example" name="example" type="text" placeholder="A sentence using it">' +

            '<label for="st-name">Your name</label>' +
            '<input id="st-name" name="name" type="text" required placeholder="So we can credit you">' +

            '<label for="st-email">Your email</label>' +
            '<input id="st-email" name="email" type="email" required placeholder="you@example.com">' +

            '<div class="modal-actions">' +
              '<button type="submit">Open email to send</button>' +
              '<span style="font-size:0.78rem;color:var(--text-faint)">or <a href="https://github.com/lukasjt/torontomansdictionary/issues/new?title=New+slang+term&body=Term%3A%0ADefinition%3A%0AExample%3A%0ASource%2Fwhere+you%27ve+heard+it%3A" target="_blank" rel="noopener">file it on GitHub</a> instead</span>' +
            '</div>' +
          '</form>' +
          '<pre class="modal-fallback" id="submit-fallback" hidden></pre>' +
        '</div>' +
      '</div>';
    document.body.appendChild(overlay);
    return overlay;
  }

  function openModal(overlay) {
    overlay.hidden = false;
    const firstInput = overlay.querySelector("#st-term");
    if (firstInput) firstInput.focus();
    document.body.style.overflow = "hidden";
  }

  function closeModal(overlay) {
    overlay.hidden = true;
    document.body.style.overflow = "";
  }

  function init() {
    const triggers = document.querySelectorAll("[data-open-submit-modal]");
    if (!triggers.length) return;

    const overlay = buildModal();
    const closeBtn = overlay.querySelector("#submit-modal-close");
    const form = overlay.querySelector("#submit-term-form");
    const fallback = overlay.querySelector("#submit-fallback");

    triggers.forEach((btn) =>
      btn.addEventListener("click", () => openModal(overlay))
    );

    closeBtn.addEventListener("click", () => closeModal(overlay));
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) closeModal(overlay);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !overlay.hidden) closeModal(overlay);
    });

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const term = (data.get("term") || "").toString().trim();
      const definition = (data.get("definition") || "").toString().trim();
      const example = (data.get("example") || "").toString().trim();
      const name = (data.get("name") || "").toString().trim();
      const email = (data.get("email") || "").toString().trim();

      const subject = "Toronto Mans Dictionary submission: " + term;
      const bodyLines = [
        "Term: " + term,
        "Definition: " + definition,
        "Example: " + (example || "(none given)"),
        "",
        "Submitted by: " + name,
        "Reply-to email: " + email,
      ];
      const body = bodyLines.join("\n");

      const mailto =
        "mailto:" + RECIPIENT +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);

      window.location.href = mailto;

      fallback.hidden = false;
      fallback.textContent =
        "If your email app didn't open, copy this and send it yourself to " + RECIPIENT + ":\n\n" +
        "Subject: " + subject + "\n\n" + body;
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
