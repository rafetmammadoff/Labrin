'use strict';
import 'bootstrap/dist/js/bootstrap';

$(function () {

  $('#toggleMenu').click(function () {
    $(this).toggleClass('active');
    $('.header-menu-mobile').slideToggle();
  });


  $('.dropdown').click(function () {
    if ($(this).hasClass('is-active')) {
      $(this).removeClass('is-active');
      $('.programs-menu').removeClass('show');
      $('.overlay').removeClass('is-show');
    } else {
      $(this).addClass('is-active');
      $('.programs-menu').addClass('show');
      $('.overlay').addClass('is-show');
    }
  });

  $('.overlay').click(function () {
    $('.dropdown').removeClass('is-active');
    $('.programs-menu').removeClass('show');
    $('.overlay').removeClass('is-show');
  });


  $("#members-section .tablinks").on('click', function(){
    console.log('clicked');
  })
});


// // TABS
// function openCity(evt, cityName) {
//   var i, tabcontent, tablinks;
//   tabcontent = document.getElementsByClassName("tabcontent");
//   for (i = 0; i < tabcontent.length; i++) {
//     // tabcontent[i].style.display = "none";

//   }
//   tablinks = document.getElementsByClassName("tablinks");
//   for (i = 0; i < tablinks.length; i++) {
//     // tablinks[i].className = tablinks[i].className.replace(" active", "");
//     // tablinks[i]
    
//   }
//   document.getElementById(cityName).style.display = "block";
//   evt.currentTarget.className += " active";

//   console.log('clicked');
// }

// Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();

