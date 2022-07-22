$(function () {

  $('.language-select').niceSelect();

  const $btn = $(".hamburger-btn");
  const $close = $("#close-navbar");
  const $menu = $(".responsive-navbar");

  $btn.on("click", () => {
    $menu.addClass("open");
  })

  $close.on("click", () => {
    $menu.removeClass("open");
  })
})

// fixed navbar
const $body = document.body || document.documentElement;
const navbar = document.querySelector(".g-nav");
const main_nav = document.querySelector(".g-nav__main");
const top_nav = document.querySelector(".g-nav__top");
const section = document.querySelector(".intro-section") || document.getElementById("g-banner-section");
const top_nav_height = top_nav.clientHeight;

const toggleFixed = () => {
  const $y = $body.scrollTop;

  if ($y > top_nav_height) {
    top_nav.classList.add('visually-hidden')
    main_nav.classList.add('fixed')
  } else {
    top_nav.classList.remove('visually-hidden')
    main_nav.classList.remove('fixed')
  }
}

$body.addEventListener("scroll", () => toggleFixed())

toggleFixed();
//footer grid

const footer = document.querySelector(".g-footer"),
  links_wrapper = footer.querySelectorAll(".g-footer__grid--item");

(function (wrapper) {
  if (window.innerWidth > 768) {
    const arr = [...wrapper].slice(0, 4);
    const gap = 80;

    const height = arr
      .map(item => item.clientHeight)
      .reduce((ctx, h) => {
        if (ctx !== undefined) {
          if (h < ctx) {
            return ctx;
          } else {
            return h;
          }
        }
      })

    document.documentElement.style.setProperty("--top-distance", (height + gap) / 16 + "rem")
  }
})(links_wrapper)

$("#searchModal").on("shown.bs.modal", function() {
  $('.modal-search input').focus()
})