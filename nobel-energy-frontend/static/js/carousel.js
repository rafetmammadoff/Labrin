const bannerCarousel = document.getElementsByClassName("intro-section__swiper")[0],
  slides = bannerCarousel.querySelectorAll(".swiper-slide"),
  newsCarousel = document.getElementsByClassName("news-section__swiper")[0],
  newsSlides = newsCarousel.querySelectorAll(".swiper-slide"),
  projectsCarousel = document.getElementsByClassName("projects-section__swiper")[0],
  projectslides = projectsCarousel.querySelectorAll(".swiper-slide"),
  businessCarousel = document.getElementsByClassName("business-section__swiper")[0],
  businessSlides = businessCarousel.querySelectorAll(".swiper-slide");

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

const bannerSwiper = new Swiper(bannerCarousel, {
  speed: 1200,
  direction: window.innerWidth > 768 ? 'vertical' : 'horizontal',
  loop: hasManySlides(slides),
  autoplay: hasManySlides(slides) ? {
    delay: 2000
  } : false,
  pagination: {
    el: '.swiper-pagination',
    type: "bullets",
    clickable: true
  },
  keyboard: {
    enabled: true,
    onlyInViewport: false,
  },
  effect: 'fade',
  fadeEffect: {
    crossFade: true
  },
})

const newsSwiper = new Swiper(newsCarousel, {
  speed: 1200,
  navigation: {
    prevEl: nav.prev,
    nextEl: nav.next,
  },
  loop: false,
  autoplay:  false,
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

const projectsSwiper = new Swiper(projectsCarousel, {
  speed: 1200,
  navigation: {
    prevEl: '#projects-prev',
    nextEl: '#projects-next',
  },
  loop: hasManySlides(newsSlides),
  autoplay: hasManySlides(projectslides) ? {
    delay: 8000
  } : false,
  spaceBetween: 20,
})

const businessSwiper = new Swiper(businessCarousel, {
  speed: 1200,
  navigation: {
    prevEl: '#business-prev',
    nextEl: '#business-next',
  },
  loop: hasManySlides(newsSlides),
  autoplay: hasManySlides(businessSlides) ? {
    delay: 2000
  } : false,
  spaceBetween: 20,
})