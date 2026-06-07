const revealItems = document.querySelectorAll(".reveal");
const header = document.querySelector("[data-elevate]");
const toast = document.querySelector("[data-toast]");
const bibtex = document.querySelector("#bibtex");
const copyButtons = document.querySelectorAll("[data-copy-bib]");

if (window.location.hash) {
  revealItems.forEach(item => item.classList.add("is-visible"));
} else if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.16 }
  );

  revealItems.forEach(item => observer.observe(item));
} else {
  revealItems.forEach(item => item.classList.add("is-visible"));
}

const elevateHeader = () => {
  if (!header) return;
  header.classList.toggle("is-elevated", window.scrollY > 10);
};

window.addEventListener("scroll", elevateHeader, { passive: true });
elevateHeader();

let toastTimer;
const showToast = () => {
  if (!toast) return;
  toast.classList.add("is-visible");
  clearTimeout(toastTimer);
  toastTimer = window.setTimeout(() => toast.classList.remove("is-visible"), 1800);
};

copyButtons.forEach(button => {
  button.addEventListener("click", async () => {
    const text = bibtex?.textContent?.trim();
    if (!text) return;

    try {
      await navigator.clipboard.writeText(text);
      showToast();
    } catch {
      const range = document.createRange();
      range.selectNodeContents(bibtex);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      showToast();
    }
  });
});
