const galleryWrapper = document.querySelector(".gallery-carousel-wrapper"),
  gallerySlides = galleryWrapper.querySelectorAll(".swiper-slide"),
  // galleryPrev = document.querySelector(".navigation-btn__prev"),
  // galleryNext = document.querySelector(".navigation-btn__next"),
  iframe = document.querySelector(".gallery-section__wrapper--iframe iframe"),
  target_video = galleryWrapper.querySelectorAll(".target-video"),
  buttons = document.querySelectorAll(".gallery-carousel .play-btn");

// const navigation = {
//   prev: galleryPrev,
//   next: galleryPrev
// }

const galleryCarousel = new Swiper(galleryWrapper, {
  speed: 1200,
  navigation: {
    prevEl: ".navigation-btn__prev",
    nextEl: ".navigation-btn__next",
  },
  breakpoints: {
    1024: {
      slidesPerView: 5,
      spaceBetween: 24,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 24,
    },
    0: {
      slidesPerView: 3,
      spaceBetween: 24,
    }
  }
});

const initGallery = () => [...buttons].forEach((btn, index) => {
  iframe.src = buttons[0].dataset.src;
  [...target_video][0].classList.add("active");

  btn.addEventListener("click", () => {
    const src = btn.dataset.src;

    [...target_video][index].classList.add("active"); 
    
    [...target_video].forEach((video, nthVideo) => {
      if (nthVideo !== index) {
        video.classList.remove("active")
      }
    })

    if (iframe.src !== src) {
      iframe.src = src;
    }
  })
})

window.onload = initGallery()