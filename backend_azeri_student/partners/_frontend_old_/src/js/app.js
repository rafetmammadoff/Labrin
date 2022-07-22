'use strict';
import 'bootstrap/dist/js/bootstrap';
import '@fancyapps/fancybox/dist/jquery.fancybox';
import 'owl.carousel/dist/owl.carousel';

$(function () {
  var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var today = new Date();
  var dd = today.getDate();
  var mm = months[today.getMonth()];
  var yy = today.getFullYear();

  $("#fallfair_pg #today").html(dd + " " + mm + " " + yy);

  $(document).on("click", "header #menu_icon", function () {
    $("header .menu").addClass("active");
  });

  $(document).on("click", "header #close_menu", function () {
    $("header .menu").removeClass("active");
  });

  $(document).on("click", "#fallfair_pg form .check_city label", function () {
    let label = $(this);
    let checkbox = label.prev();
    let counter = label.parents(".check_city").find("input[type='number']");

    if (!checkbox.is(":checked")) {
      counter.removeAttr("disabled");
    } else {
      counter.attr("disabled", "disabled");
      counter.val("1");
    }
  });

  $("#fallfair_pg #participants .owl-carousel").owlCarousel({
    items: 1,
    loop: true,
    responsive: {
      0: {
        items: 1
      },

      768: {
        items: 2
      },

      992: {
        items: 3
      }
    }
  })
});


// back
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



    $('.register-submit-form').submit(function (e) {
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
                base_form.find("input[type=text], input[type=email], textarea").val("");
                base_form.find("input[type=text], input[type=email], textarea").css("box-shadow", "none");
                show_snackbar("Successfully registered");
                $("input[type=checkbox]:checked").prop('checked', false);
                $("input[type=number]").val(1);
                $('.nonform').attr('disabled',true);
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



