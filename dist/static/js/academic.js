// ============================================================
// Research Portfolio: minimal interaction layer.
// Mobile nav, smooth scroll, theme toggle, contact form.
// ============================================================

(function () {
    'use strict';

    // ---- Apply persisted theme as early as possible (in addition to inline head script) ----
    try {
        var saved = localStorage.getItem('vc-theme');
        var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        var initial = saved || (prefersDark ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', initial);
    } catch (e) {}

    function setThemeIcon(button, theme) {
        if (!button) return;
        var icon = button.querySelector('i');
        if (!icon) return;
        icon.classList.remove('fa-sun', 'fa-moon');
        icon.classList.add(theme === 'dark' ? 'fa-sun' : 'fa-moon');
    }

    document.addEventListener('DOMContentLoaded', function () {

        // ---- Theme toggle ----
        var themeButtons = document.querySelectorAll('.theme-toggle');
        var currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        themeButtons.forEach(function (btn) {
            setThemeIcon(btn, currentTheme);
            btn.addEventListener('click', function () {
                var now = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                document.documentElement.setAttribute('data-theme', now);
                try { localStorage.setItem('vc-theme', now); } catch (e) {}
                themeButtons.forEach(function (b) { setThemeIcon(b, now); });
            });
        });

        // ---- Mobile navigation toggle ----
        var navContainer = document.querySelector('.nav-container');
        var navMenu = document.querySelector('.nav-menu');
        if (navContainer && navMenu && !document.querySelector('.nav-toggle')) {
            var toggle = document.createElement('button');
            toggle.type = 'button';
            toggle.className = 'nav-toggle';
            toggle.setAttribute('aria-label', 'Toggle navigation');
            toggle.innerHTML = '<i class="fas fa-bars"></i>';
            navContainer.appendChild(toggle);

            toggle.addEventListener('click', function (e) {
                e.stopPropagation();
                navMenu.classList.toggle('nav-menu-open');
                var icon = toggle.querySelector('i');
                if (icon) {
                    icon.classList.toggle('fa-bars');
                    icon.classList.toggle('fa-times');
                }
            });

            document.querySelectorAll('.nav-link').forEach(function (link) {
                link.addEventListener('click', function () {
                    navMenu.classList.remove('nav-menu-open');
                    var icon = toggle.querySelector('i');
                    if (icon) {
                        icon.classList.add('fa-bars');
                        icon.classList.remove('fa-times');
                    }
                });
            });

            document.addEventListener('click', function (e) {
                if (!navContainer.contains(e.target) && navMenu.classList.contains('nav-menu-open')) {
                    navMenu.classList.remove('nav-menu-open');
                    var icon = toggle.querySelector('i');
                    if (icon) {
                        icon.classList.add('fa-bars');
                        icon.classList.remove('fa-times');
                    }
                }
            });
        }

        // ---- Smooth scroll with sticky-nav offset ----
        document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
            var href = anchor.getAttribute('href');
            if (!href || href === '#' || href.length < 2) return;
            anchor.addEventListener('click', function (e) {
                var target = document.querySelector(href);
                if (!target) return;
                e.preventDefault();
                var navHeight = (document.querySelector('.navbar') || {}).offsetHeight || 0;
                var top = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 12;
                window.scrollTo({ top: top, behavior: 'smooth' });
            });
        });

        // ---- Contact form ----
        var form = document.getElementById('contactForm');
        if (form) {
            var formMessage = document.getElementById('formMessage');
            var endpoint = form.getAttribute('data-action') || form.getAttribute('action') || '/contact';
            form.addEventListener('submit', function (e) {
                e.preventDefault();
                if (!formMessage) return;
                formMessage.style.display = 'none';

                var formData = {
                    name: form.querySelector('[name="name"]').value.trim(),
                    email: form.querySelector('[name="email"]').value.trim(),
                    subject: form.querySelector('[name="subject"]').value.trim(),
                    message: form.querySelector('[name="message"]').value.trim(),
                };

                if (!formData.name || !formData.email || !formData.subject || !formData.message) {
                    formMessage.textContent = 'Please fill in all fields.';
                    formMessage.className = 'form-message error';
                    formMessage.style.display = 'block';
                    return;
                }

                fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData),
                })
                    .then(function (r) { return r.json().catch(function () { return { success: false }; }); })
                    .then(function (data) {
                        if (data && data.success) {
                            formMessage.textContent = data.message || 'Message sent. Thank you.';
                            formMessage.className = 'form-message success';
                            form.reset();
                        } else {
                            formMessage.textContent = (data && data.message) || 'Could not send the message.';
                            formMessage.className = 'form-message error';
                        }
                        formMessage.style.display = 'block';
                    })
                    .catch(function () {
                        formMessage.textContent = 'Network error. Please email directly.';
                        formMessage.className = 'form-message error';
                        formMessage.style.display = 'block';
                    });
            });
        }

        // ---- Scroll-reveal via IntersectionObserver ----
        if ('IntersectionObserver' in window) {
            var revealObserver = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        revealObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

            var revealSelectors = [
                '.interest-card', '.pub-item', '.project-card',
                '.experience-item', '.education-card', '.skill-category',
                '.teaching-list li', '.section-header'
            ];
            revealSelectors.forEach(function (sel) {
                document.querySelectorAll(sel).forEach(function (el) {
                    el.classList.add('reveal');
                    revealObserver.observe(el);
                });
            });
        }
    });
})();
