/* Evidence paths: progressive enhancement. Everything remains readable without JS. */
(function () {
  'use strict';
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const cleanups = [];
  let lenis = null;
  let motionContext = null;
  let networkPaused = false;
  let activeFocus = 'llm';
  const notes = {
    llm: 'Trace a generated answer back to its source. Hierarchical RAG preserves context and supporting evidence.',
    reasoning: 'Test for structure, not shortcuts. Sanskrit benchmarks and neuro-symbolic systems probe what models really learn.',
    agents: 'Learn to act together. Graph-based communication connects autonomous vehicles with coordinated, safety-aware decisions.'
  };
  const listen = (element, name, fn) => {
    if (!element) return;
    element.addEventListener(name, fn);
    cleanups.push(() => element.removeEventListener(name, fn));
  };

  function selectFocus(focus) {
    activeFocus = focus;
    document.querySelectorAll('[data-focus]').forEach(el => el.setAttribute('aria-pressed', String(el.dataset.focus === focus)));
    document.querySelectorAll('[data-node], [data-path]').forEach(el => el.classList.toggle('is-active', (el.dataset.node || el.dataset.path) === focus));
    document.querySelectorAll('[data-flow]').forEach(el => { el.style.opacity = el.dataset.flow === focus ? '1' : '0'; });
    const note = document.querySelector('.network-note');
    if (note) note.textContent = notes[focus];
    const projectLink = document.querySelector('.network-project-link');
    if (projectLink) {
      projectLink.href = projectLink.getAttribute('data-project-' + focus);
      projectLink.firstChild.textContent = {llm: 'Explore H-RAG ', reasoning: 'Explore SanskritEval ', agents: 'Explore CMARL '}[focus];
    }
  }

  function initInteractions() {
    const themeButton = document.querySelector('.theme-toggle');
    const syncTheme = () => themeButton?.setAttribute('aria-label', document.documentElement.dataset.theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    syncTheme();
    listen(themeButton, 'click', () => {
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.classList.add('theme-changing');
      document.documentElement.dataset.theme = next;
      // Resolve all semantic colors together, avoiding low-contrast intermediate states.
      void document.documentElement.offsetHeight;
      document.documentElement.classList.remove('theme-changing');
      try { localStorage.setItem('vc-theme', next); } catch (_) {}
      syncTheme();
    });

    const menuButton = document.querySelector('.menu-toggle');
    const menu = document.querySelector('#mobile-menu');
    const setMenu = (open, restoreFocus = false) => {
      if (!menu || !menuButton) return;
      menu.hidden = !open;
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.innerHTML = open ? 'Close <span aria-hidden="true">×</span>' : 'Menu <span aria-hidden="true">+</span>';
      document.body.classList.toggle('menu-open', open);
      if (open) { lenis?.stop(); menu.querySelector('a')?.focus(); }
      else { lenis?.start(); if (restoreFocus) menuButton.focus(); }
    };
    listen(menuButton, 'click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true', true));
    listen(document, 'keydown', e => {
      if (!menu || menu.hidden) return;
      if (e.key === 'Escape') setMenu(false, true);
      if (e.key === 'Tab') {
        const items = [menuButton, ...menu.querySelectorAll('a')];
        const first = items[0], last = items[items.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    listen(window, 'resize', () => { if (window.innerWidth > 820 && menu && !menu.hidden) setMenu(false); });
    document.querySelectorAll('#mobile-menu a').forEach(link => listen(link, 'click', () => setMenu(false)));

    document.querySelectorAll('[data-focus]').forEach(button => listen(button, 'click', () => selectFocus(button.dataset.focus)));
    selectFocus(activeFocus);
    const pause = document.querySelector('.motion-toggle');
    const syncPause = () => {
      if (!pause) return;
      pause.disabled = reduced.matches;
      pause.setAttribute('aria-pressed', String(networkPaused || reduced.matches));
      pause.innerHTML = reduced.matches ? 'Motion reduced' : networkPaused ? 'Play motion <span aria-hidden="true">▷</span>' : 'Pause motion <span aria-hidden="true">Ⅱ</span>';
    };
    listen(pause, 'click', () => { networkPaused = !networkPaused; syncPause(); });
    listen(reduced, 'change', syncPause);
    syncPause();

    const rows = [...document.querySelectorAll('.project-row[data-category]')];
    document.querySelectorAll('[data-filter]').forEach(button => listen(button, 'click', () => {
      const category = button.dataset.filter;
      document.querySelectorAll('[data-filter]').forEach(el => el.setAttribute('aria-pressed', String(el === button)));
      let shown = 0;
      rows.forEach(row => {
        row.hidden = category !== 'all' && row.dataset.category !== category;
        if (!row.hidden) shown++;
      });
      const counter = document.getElementById('project-count');
      if (counter) counter.textContent = shown + (shown === 1 ? ' project' : ' projects');
      window.ScrollTrigger?.refresh();
    }));

    document.querySelectorAll('[data-dialog]').forEach(button => {
      const dialog = document.getElementById(button.dataset.dialog);
      if (!dialog) return;
      listen(button, 'click', () => { lenis?.stop(); dialog.showModal(); document.body.classList.add('dialog-open'); });
      const close = () => dialog.close();
      listen(dialog.querySelector('.dialog-close'), 'click', close);
      listen(dialog, 'click', e => { if (e.target === dialog) { const r = dialog.getBoundingClientRect(); if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) close(); } });
      listen(dialog, 'close', () => { document.body.classList.remove('dialog-open'); lenis?.start(); button.focus(); });
    });

    document.querySelectorAll('a[href]').forEach(link => listen(link, 'click', e => {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || link.target || link.hasAttribute('download')) return;
      const url = new URL(link.href, window.location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) {
        const id = decodeURIComponent(url.hash.slice(1));
        const target = document.getElementById(id);
        if (!target) return;
        e.preventDefault();
        if (target.tagName === 'DETAILS') target.open = true;
        history.pushState(null, '', url.hash);
        if (lenis && !reduced.matches) lenis.scrollTo(target, { offset: -100, duration: 1 });
        else target.scrollIntoView({ behavior: 'instant' });
        target.setAttribute('tabindex', '-1');
        target.focus({ preventScroll: true });
      } else if (!url.hash && url.pathname === location.pathname) {
        return;
      } else if (/\.html$/.test(url.pathname) || !/\.[a-z0-9]+$/i.test(url.pathname)) {
        if (!window.gsap || reduced.matches) return;
        e.preventDefault();
        const curtain = document.querySelector('.transition-panel');
        if (!curtain) { location.assign(url.href); return; }
        window.gsap.fromTo(curtain, { autoAlpha: 1, clipPath: 'inset(100% 0 0 0)' }, { clipPath: 'inset(0% 0 0 0)', duration: .25, ease: 'power3.inOut', onComplete: () => { try { sessionStorage.setItem('vc-transition', '1'); } catch (_) {} location.assign(url.href); } });
      }
    }));
    listen(document, 'toggle', e => { if (e.target.tagName === 'DETAILS') window.ScrollTrigger?.refresh(); });
  }

  // All animation is registered in one page lifecycle and uses GSAP's ticker.
  function onPage() {
    const gsap = window.gsap;
    if (!gsap || reduced.matches) return () => {};
    const curtain = document.querySelector('.transition-panel');
    if (document.documentElement.classList.contains('page-entering') && curtain) {
      try { sessionStorage.removeItem('vc-transition'); } catch (_) {}
      gsap.fromTo(curtain, {autoAlpha: 1, clipPath: 'inset(0 0 0% 0)'}, {
        clipPath: 'inset(0 0 100% 0)', duration: .4, ease: 'power3.inOut',
        onComplete: () => { document.documentElement.classList.remove('page-entering'); gsap.set(curtain,{autoAlpha:0}); }
      });
    }
    const ScrollTrigger = window.ScrollTrigger;
    if (ScrollTrigger) gsap.registerPlugin(ScrollTrigger);
    const teardown = [];
    if (window.Lenis) {
      lenis = new window.Lenis({ autoRaf: false, smoothWheel: true, lerp: .12, anchors: false });
      const tickScroll = time => lenis?.raf(time * 1000);
      gsap.ticker.add(tickScroll);
      if (ScrollTrigger) lenis.on('scroll', ScrollTrigger.update);
      teardown.push(() => { gsap.ticker.remove(tickScroll); lenis?.destroy(); lenis = null; });
    }
    motionContext = gsap.context(() => {
      const intro = gsap.timeline({ defaults: { ease: 'power3.out' } });
      // Headline stays in the first paint; only the supporting composition is traced in.
      intro.from('.network-card', { clipPath: 'inset(0 0 100% 0)', duration: .85, clearProps: 'clipPath' }, 0);
      intro.from('.hero-location', { y: 10, opacity: 0, duration: .65, clearProps: 'all' }, .15);
      if (ScrollTrigger) {
        document.querySelectorAll('[data-bar]').forEach(bar => {
          gsap.fromTo(bar, { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: '.study-chart', start: 'top 85%', once: true } });
        });
        document.querySelectorAll('[data-result-bar]').forEach(bar => {
          gsap.fromTo(bar, {clipPath:'inset(0 100% 0 0)'}, {
            clipPath:'inset(0 0% 0 0)', duration:1.1, ease:'power3.out',
            scrollTrigger:{trigger:'.published-chart',start:'top 85%',once:true}
          });
        });
        const navs = [...document.querySelectorAll('.desktop-nav a')];
        ['projects', 'publications', 'experience', 'contact'].forEach(id => {
          const section = document.getElementById(id);
          if (!section) return;
          const mark = () => navs.forEach(link => { if (link.hash === '#' + id) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
          ScrollTrigger.create({ trigger: section, start: 'top 30%', end: 'bottom 30%', onEnter: mark, onEnterBack: mark });
        });
      }
    });
    const network = document.querySelector('[data-network]');
    if (network) {
      let visible = true;
      const observer = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; }, { threshold: .05 });
      observer.observe(network);
      const flows = [...network.querySelectorAll('[data-flow]')];
      const ring = network.querySelector('.core-ring');
      if (ring) gsap.set(ring, { svgOrigin: '270 175' });
      let phase = 0;
      const tickNetwork = (_time, delta) => {
        if (!visible || networkPaused || document.hidden) return;
        phase = (phase + Math.min(delta, 50) * .025) % 132;
        flows.forEach(path => { if (path.dataset.flow === activeFocus) path.style.strokeDashoffset = String(-phase); });
        if (ring) gsap.set(ring, { scale: 1 + Math.sin(phase * Math.PI / 66) * .06 });
      };
      gsap.ticker.add(tickNetwork);
      teardown.push(() => { observer.disconnect(); gsap.ticker.remove(tickNetwork); });
    }
    return () => { teardown.forEach(fn => fn()); motionContext?.revert(); motionContext = null; };
  }

  let disposeMotion = () => {};
  function init() {
    initInteractions();
    disposeMotion = onPage();
    if (!window.gsap || reduced.matches) document.documentElement.classList.remove('page-entering');
    try { sessionStorage.removeItem('vc-transition'); } catch (_) {}
    listen(reduced, 'change', () => { disposeMotion(); disposeMotion = onPage(); });
    listen(window, 'pageshow', event => {
      if (!event.persisted) return;
      document.documentElement.classList.remove('page-entering');
      const curtain = document.querySelector('.transition-panel');
      if (curtain) { curtain.style.visibility = 'hidden'; curtain.style.opacity = '0'; }
    });
    if (location.hash) {
      const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target?.tagName === 'DETAILS') target.open = true;
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
