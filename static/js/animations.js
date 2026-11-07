/* ============================================================
   Portfolio CMS — Animations JavaScript
   ============================================================ */

// -- Intersection Observer for reveal animations ------------
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, index) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, index * 80);
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// -- Animated number counter -------------------------------
function animateCounter(el, target, duration = 1800) {
  let start = 0;
  const increment = target / (duration / 16);
  const update = () => {
    start += increment;
    if (start < target) {
      el.textContent = Math.floor(start) + (el.dataset.suffix || '+');
      requestAnimationFrame(update);
    } else {
      el.textContent = target + (el.dataset.suffix || '+');
    }
  };
  requestAnimationFrame(update);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.target || el.textContent, 10);
      if (!isNaN(target)) animateCounter(el, target);
      counterObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.counter-num').forEach(el => counterObserver.observe(el));

// -- Skill bar animation ------------------------------------
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const fills = entry.target.querySelectorAll('.skill-level-fill');
      fills.forEach(fill => {
        const width = fill.dataset.width || fill.style.width;
        fill.style.width = '0';
        setTimeout(() => { fill.style.width = width; }, 100);
      });
      skillObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.skill-grid').forEach(grid => skillObserver.observe(grid));

// -- Typing effect for hero ---------------------------------
const typingEl = document.getElementById('hero-typing');
if (typingEl) {
  const texts = JSON.parse(typingEl.dataset.texts || '[]');
  let textIdx = 0, charIdx = 0, deleting = false;
  function type() {
    if (!texts.length) return;
    const current = texts[textIdx];
    if (deleting) {
      typingEl.textContent = current.substring(0, charIdx--);
      if (charIdx < 0) { deleting = false; textIdx = (textIdx + 1) % texts.length; setTimeout(type, 500); return; }
    } else {
      typingEl.textContent = current.substring(0, ++charIdx);
      if (charIdx === current.length) { deleting = true; setTimeout(type, 2000); return; }
    }
    setTimeout(type, deleting ? 60 : 100);
  }
  setTimeout(type, 1000);
}
