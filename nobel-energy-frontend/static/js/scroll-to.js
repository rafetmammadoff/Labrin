const toSection = document.querySelectorAll(".scroll-to");
const toTop = document.getElementById("scroll-top");

const nav_height = navbar.clientHeight;
const main_height = main_nav.clientHeight;

const scrollToSection = btn => {
  const target = btn.dataset.target;

  const el = document.getElementById(target)

  // document.documentElement.style.setProperty('--scroll-padding', window.scrollY > nav_height ? 100 + "px" : 150 + "px")

  // const top = window.scrollY > nav_height ? 100 + "px" : 150 + "px";

  el.scrollIntoView({
    behavior: "smooth",
    inline: "start",
    block: "start"
  })
};

// if (window.innerWidth > 768) {
//   [...toSection].forEach(btn => {
//     btn.addEventListener("click", () => scrollToSection(btn))
//   });
// } else {
  $('.scroll-to').on('click', function (e) {
    const margin = parseFloat($(`#${$(this).data("target")}`).css("marginTop"))
    const $nav_height = parseFloat($('.g-nav__main').css("height"))
    const banner_height= parseFloat($("#section-to").css("height"))

    console.log(margin + $nav_height + banner_height - 80)
    $('body').stop().animate({
      scrollTop: margin + $nav_height + banner_height - 80
    }, 1000, 'linear');
  });
// }


toTop.addEventListener("click", () => {
  window.scroll({
    behavior: "smooth",
    top: 0,
    left: 0
  })
})

