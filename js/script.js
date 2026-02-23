(function () {
  var toggle = document.querySelector('.nav-toggle');
  var navMobile = document.querySelector('.nav-mobile');
  if (!toggle || !navMobile) return;

  toggle.addEventListener('click', function () {
    var open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !open);
    navMobile.classList.toggle('is-open', !open);
    document.body.style.overflow = open ? '' : 'hidden';
  });

  navMobile.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      toggle.setAttribute('aria-expanded', 'false');
      navMobile.classList.remove('is-open');
      document.body.style.overflow = '';
    });
  });
})();
