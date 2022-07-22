'use strict';
import 'bootstrap/dist/js/bootstrap';
import '@fancyapps/fancybox/dist/jquery.fancybox';
import 'owl.carousel2/dist/owl.carousel';

$(function () {
  //MENU BUTTON TRANSFORM TO X AND TOGGLE MENU
  $('#toggleMenuButton').click(function () {
    $(this).toggleClass('active');
    $('.toggle_menu').slideToggle();
    $('body').toggleClass('active');
  });
    //MENU BUTTON TRANSFORM TO X AND TOGGLE MENU

});
$(function () {
  // ------------- CART - INCREMENT/DECREMENT QUANTITY ------------- //
  $(document).on('click', '.selected-cart-item .increase', function () {
    console.log($(this));
    console.log($(this).siblings('.amount'))
    $(this).siblings('.amount').val(function (i, oldval) {
      return ++oldval;
    });
  });
  $(document).on('click', '.selected-cart-item .decrease', function () {
    if ($(this).siblings('.amount').val() > 0) {
      $(this).siblings('.amount').val(function (i, oldval) {
        return --oldval;
      });
    }
  });
  $(document).on('keydown', '.selected-cart-item .amount', function (e) {
    if ((e.keyCode === 189) || (e.keyCode === 187)) {
      return false;
    }
  });
});
  // ------------- CART - INCREMENT/DECREMENT QUANTITY ------------- //

$(function () {
  $(".button-spring").click(function () {
    $(this).toggleClass("active");
  });
});

$(function () {
  // $('#accept').click(function () {
  //   if ($('.accept').is(':disabled')) {
  //     $('.accept').removeAttr('disabled');
  //   } else {
  //     $('.accept').attr('disabled', 'disabled');
  //   }
  // });
  // $('#accept1').click(function () {
  //   if ($('.accept-1').is(':disabled')) {
  //     $('.accept-1').removeAttr('disabled');
  //   } else {
  //     $('.accept-1').attr('disabled', 'disabled');
  //   }
  // });
  // $('#accept2').click(function () {
  //   if ($('.accept-2').is(':disabled')) {
  //     $('.accept-2').removeAttr('disabled');
  //   } else {
  //     $('.accept-2').attr('disabled', 'disabled');
  //   }
  // });
  // $('#accept3').click(function () {
  //   if ($('.accept-3').is(':disabled')) {
  //     $('.accept-3').removeAttr('disabled');
  //   } else {
  //     $('.accept').attr('disabled', 'disabled');
  //   }
  // });

  // spring fair register
  $('.button-spring').click(function () {
    const city = $(this).data('city');

    const target = $(`.selected-cart-item[data-city='${city}'] button`);
    const table_count_input = $('.amount');
    table_count_input.removeAttr('disabled');
    if (target.is(':disabled')) {
      target.removeAttr('disabled');
    } else {
      target.attr('disabled', 'disabled');
    }
  })

/*============== Ajax helper csrf_token generate ajax methods =============*/

  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  function show_snackbar(text) {
      // Get the snackbar DIV
      var x = document.getElementById("snackbar");
      // set snackbar text
      x.innerHTML = text;
      // Add the "show" class to DIV
      x.className = "show";
      // After 5 seconds, remove the show class from DIV
      setTimeout(function () {
          x.className = x.className.replace("show", "");
      }, 5000);
  }

// spring fair register //
// spring fair carousel 
  $(document).ready(function () {
    /*============== Ajax Setup csrf_token generate ajax headers =============*/
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", $("#csrfmiddlewaretoken").val());
            }
        }
    });


    $('.previous-exhibitions-image .owl-carousel').owlCarousel({
      loop: false,
      dots: true,
      nav: false,
      responsive: {
        0: {
          items: 1.5
        },
        576: {
          items: 2
        },
        767: {
          items: 4
        },
        1200: {
          items: 7
        }
      }
    });

    // spring fair carousel  //
    // spring fair comment  

    $('.spring-fair-comment .owl-carousel').owlCarousel({
      loop: true,
      nav: false,
      margin:10,
      navText: ["<img src='../../../static/partners/assets/left.png'>", "<img src='../../../static/partners/assets/right.png'>"],
      responsive: {
        0: {
          items: 1
        }
      }
    });



    $('.register-submit-form').submit(function (e) {
        console.log('Submit btn worked!');
    var base_form = $(this);
    var data = $(this).serialize();
    var url = $(this).data('action');
    e.preventDefault();
    $.ajax({
        url: url,
        type: "POST",
        data: data,
        success: function (data) {
            if (data.save) {
                // base_form.find("input[type=text], input[type=email], textarea").val("");
                // base_form.find("input[type=text], input[type=email], textarea").css("box-shadow", "none");
                show_snackbar("Successfully registered!");
                // $("input[type=checkbox]:checked").prop('checked', false);
                // $("input[type=number]").val(1);
                // $('.nonform').attr('disabled',true);
            } else {
                show_snackbar("Error");
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr, errmsg, err);
        } // end error: function
    });

    return false;
    });
  });

// spring fair comment  //
//  fancybox
$(document).ready(function() {
		$(".fancybox").fancybox();
  });
  //  fancybox

})
