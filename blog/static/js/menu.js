const header = document.querySelector('.blog-header');
let lastScrollY = 0;

window.addEventListener('scroll', () => {
  const currentScrollY = window.pageYOffset;

  if (currentScrollY > lastScrollY) {
    header.style.opacity = '0';
  } else {
    header.style.opacity = '1';
  }

  lastScrollY = currentScrollY;
});

window.addEventListener('scroll', function() {
  var header = document.querySelector('.blog-header');
  var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

  if (scrollTop > 200) {
    header.classList.add('hidden');
  } else {
    header.classList.remove('hidden');
  }
});