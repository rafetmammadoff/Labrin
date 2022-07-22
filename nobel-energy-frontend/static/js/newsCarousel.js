const newsCarousel = document.getElementsByClassName("news-section__swiper")[0],
  newsSlides = newsCarousel.querySelectorAll(".swiper-slide");

const nav = {
  prev: "#news-prev-md",
  next: "#news-next-md"
}

window.addEventListener("resize", () => {
  if (window.innerWidth <= 768) {
    nav.prev = "#news-prev-sm"
    nav.next = "#news-next-sm"
  } else {
    nav.prev = "#news-prev-md"
    nav.next = "#news-next-md"
  }
})

const hasManySlides = slides => {
  if (slides.length > 1) {
    return true
  } else {
    return false
  }
};


const newsSwiper = new Swiper(newsCarousel, {
  speed: 1200,
  navigation: {
    prevEl: nav.prev,
    nextEl: nav.next,
  },
  loop: false,
  autoplay: false,
  breakpoints: {
    1100: {
      slidesPerView: 3,
      spaceBetween: 24,
    },
    728: {
      slidesPerView: 2,
      spaceBetween: 24,
    },
    0: {
      slidesPerView: 1,
      spaceBetween: 24,
    }
  }
});