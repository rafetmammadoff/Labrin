var swiper = new Swiper('.main-swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    loopFillGroupWithBlank: true,
    speed: 1500,
    autoplay: {
        delay: 500,
        disableOnInteraction: false,
    },
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
  // Responsive breakpoints
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 1,
      spaceBetween: 30
    },
    // when window width is >= 640px
    640: {
      slidesPerView: 2,
      spaceBetween: 40
    },
    992: {
        slidesPerView: 3,
        spaceBetween: 40
      }
  }
    
});




 
  
  var clientswiper = new Swiper('.client-swipper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    loop: true,
    loopFillGroupWithBlank: true,
    speed: 1500,
    autoplay: {
        delay: 500,
        disableOnInteraction: false,
    },
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
  // Responsive breakpoints
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 2,
      spaceBetween: 20
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 3,
      spaceBetween: 20
    },
    // when window width is >= 640px
    768: {
      slidesPerView: 4,
      spaceBetween: 20
    },
    1240: {
        slidesPerView: 6,
      spaceBetween: 20
    }
  }
    
  });  
  

var hrswiper = new Swiper(".hero-slide", {
    loop: true,
    loopFillGroupWithBlank: true,
    speed: 1500,
    autoplay: {
        delay: 3500,
        disableOnInteraction: true,
    }
});


var teamswiper = new Swiper('.team-swipper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    loop: true,
    loopFillGroupWithBlank: true,
    speed: 1500,
    autoplay: {
        delay: 500,
        disableOnInteraction: false,
    },
  
    // If we need pagination
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
  
  // Responsive breakpoints
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 3,
      spaceBetween: 20
    },
    // when window width is >= 640px
    640: {
      slidesPerView: 6,
      spaceBetween: 20
    }
  }
    
  });  


  var blurPage=document.querySelector("#blur-page")
  function myFunction() {
    

    blurPage.classList.toggle("bluur")
  }



