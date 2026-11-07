/* ============================================================
   Portfolio CMS — Main JavaScript
   ============================================================ */

// -- Navbar scroll effect -----------------------------------
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  });
}

// -- Django messages auto-dismiss --------------------------
document.addEventListener('DOMContentLoaded', () => {
  const toasts = document.querySelectorAll('.alert-toast');
  toasts.forEach(toast => {
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(20px)';
      toast.style.transition = 'all 0.4s ease';
      setTimeout(() => toast.remove(), 400);
    }, 4000);
  });
});

// -- Smooth scroll for anchor links ------------------------
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// -- Active nav link highlighting --------------------------
const currentPath = window.location.pathname;
document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});

// -- Contact form loading state ----------------------------
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', function() {
    if (typeof this.checkValidity === 'function' && !this.checkValidity()) return;
    const btn = this.querySelector('[type="submit"]');
    if (btn) {
      setTimeout(() => {
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Sending…';
        btn.disabled = true;
      }, 0);
    }
  });
}

// -- Project category filter --------------------------------
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-item');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    projectCards.forEach(card => {
      const match = filter === 'all' || card.dataset.category === filter;
      card.style.opacity = match ? '1' : '0.2';
      card.style.pointerEvents = match ? 'auto' : 'none';
      card.style.transform = match ? 'scale(1)' : 'scale(0.95)';
      card.style.transition = 'all 0.3s ease';
    });
  });
});
