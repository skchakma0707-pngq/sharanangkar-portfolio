/* ===================================================
   SHARANANNGKAR CHAKMA — PORTFOLIO JAVASCRIPT
   =================================================== */

/* ---- CURSOR GLOW ---- */
const cursorGlow = document.getElementById('cursorGlow');
document.addEventListener('mousemove', (e) => {
  cursorGlow.style.left = e.clientX + 'px';
  cursorGlow.style.top  = e.clientY + 'px';
});

/* ---- NAVBAR SCROLL ---- */
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
  updateActiveNav();
});

/* ---- MOBILE NAV TOGGLE ---- */
const navToggle  = document.getElementById('navToggle');
const navLinks   = document.getElementById('navLinks');
navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});
navLinks.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

/* ---- ACTIVE NAV LINK ON SCROLL ---- */
function updateActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 200) {
      current = section.getAttribute('id');
    }
  });
  document.querySelectorAll('.nav-link').forEach(link => {
    link.classList.toggle('active', link.dataset.section === current);
  });
}

/* ---- FLOATING PARTICLES ---- */
const particlesContainer = document.getElementById('particles');
const PARTICLE_COLORS = ['rgba(0,230,175,', 'rgba(61,127,255,', 'rgba(124,58,237,'];
const NUM_PARTICLES = 35;

for (let i = 0; i < NUM_PARTICLES; i++) {
  createParticle();
}
function createParticle() {
  const p = document.createElement('div');
  p.classList.add('particle');
  const size    = Math.random() * 5 + 1;
  const x       = Math.random() * 100;
  const dur     = Math.random() * 15 + 8;
  const delay   = Math.random() * 12;
  const color   = PARTICLE_COLORS[Math.floor(Math.random() * PARTICLE_COLORS.length)];
  const opacity = Math.random() * 0.5 + 0.1;
  p.style.cssText = `
    width: ${size}px;
    height: ${size}px;
    left: ${x}%;
    background: ${color}${opacity});
    animation-duration: ${dur}s;
    animation-delay: ${delay}s;
    box-shadow: 0 0 ${size * 3}px ${color}0.5);
  `;
  particlesContainer.appendChild(p);
}

/* ---- INTERSECTION OBSERVER — REVEAL ---- */
const revealEls = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });
revealEls.forEach(el => revealObserver.observe(el));

/* ---- COUNTER ANIMATION ---- */
function animateCounter(el, target, duration = 1500) {
  let start = 0;
  const step = Math.ceil(target / (duration / 16));
  const interval = setInterval(() => {
    start = Math.min(start + step, target);
    el.textContent = start + (target >= 10 ? '+' : '');
    if (start >= target) clearInterval(interval);
  }, 16);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      animateCounter(el, target);
      counterObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('.stat-number').forEach(el => counterObserver.observe(el));

/* ---- SKILL BAR ANIMATION ---- */
const skillBarObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const bar = entry.target;
      const width = bar.dataset.width;
      setTimeout(() => { bar.style.width = width + '%'; }, 200);
      skillBarObserver.unobserve(bar);
    }
  });
}, { threshold: 0.3 });
document.querySelectorAll('.skill-bar').forEach(el => skillBarObserver.observe(el));

/* ---- CONTACT FORM ---- */
const contactForm = document.getElementById('contactForm');
const formSuccess = document.getElementById('formSuccess');
const submitBtn   = document.getElementById('submitBtn');

contactForm.addEventListener('submit', (e) => {
  e.preventDefault();
  submitBtn.disabled = true;
  submitBtn.querySelector('span').textContent = 'Sending...';

  // Simulate send (replace with real email service if needed)
  setTimeout(() => {
    formSuccess.style.display = 'block';
    contactForm.reset();
    submitBtn.disabled = false;
    submitBtn.querySelector('span').textContent = 'Send Message';
    setTimeout(() => { formSuccess.style.display = 'none'; }, 4000);
  }, 1200);
});

/* ---- SMOOTH SCROLL FOR NAV LINKS ---- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

/* ---- PAGE LOAD STAGGER FOR HERO ---- */
window.addEventListener('load', () => {
  const heroItems = document.querySelectorAll('.hero-content .reveal-up, .hero-avatar.reveal-right');
  heroItems.forEach((el, i) => {
    setTimeout(() => {
      el.classList.add('visible');
    }, 200 + i * 130);
  });
});


