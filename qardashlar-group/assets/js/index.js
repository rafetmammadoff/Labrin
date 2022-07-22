//CLOSE NAVBAR
document.querySelectorAll(".nav-item").forEach((item) => {
  item.onclick = () => {
      if (window.innerWidth < 1200) {
          document.querySelector(".navbar-toggler").click()
      }
  }
})


// SWIPER SLIDE
var swiper = new Swiper(".hero-sldie", {
    loop: true,
    loopFillGroupWithBlank: true,
    speed: 1500,
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    }
});

var swiper = new Swiper(".projects-slide", {
  slidesPerView: 2,
  grid: {
    rows: 2,
  },
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    768: {
        grid: {
            rows: 2,
          },
        slidesPerView: 3,
    },
    992: {
        grid: {
            rows: 2,
          },
        slidesPerView: 4,
    },
},
});


// TAB
function openTab(evt, index) {
  var i, tabcontent, tablinks;

  tabcontent = document.querySelectorAll(".projects-slide");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.querySelectorAll(".tab-links");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById(index).style.display = "flex";
  evt.currentTarget.className += " active";

}
document.getElementById("active-tab").click();


// COUNTER
counter()
function counter() {
    var oTop;
    if ($('.data-number').length !== 0) {
        oTop = $('.data-number').offset().top - window.innerHeight;
    }

    if ($(window).scrollTop() > oTop) {
        $('.data-number').each(function () {
            var $this = $(this),
                countTo = $this.attr('data-count');
            $({
                countNum: $this.text()
            }).animate({
                countNum: countTo
            }, {
                duration: 3000,
                easing: 'swing',
                step: function () {
                    $this.text(Math.floor(this.countNum));
                },
                complete: function () {
                    $this.text(this.countNum);
                }
            });
        });
    }
}
$(window).on('scroll', function () {
  counter()
})
