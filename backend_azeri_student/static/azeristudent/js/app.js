App.js
(function() {


}).call(this);

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

csrftoken = getCookie('csrftoken');

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
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    var divElement = $('div');
    var wow = new WOW({
        boxClass: 'wow', // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset: 0, // distance to the element when triggering the animation (default is 0)
        mobile: true, // trigger animations on mobile devices (default is true)
        live: true, // act on asynchronously loaded content (default is true)
        callback: function (box) {
            // the callback is fired every time an animation is started
            // the argument that is passed in is the DOM node being animated
        },
        scrollContainer: null // optional scroll container selector, otherwise use window
    });
    wow.init();

    $('.slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: true,
        items: 1,
        navText: ["<img src='/static/azeristudent/img/back.png'>", "<img src='/static/azeristudent/img/next.png'>"],
        autoplay: true,
        autoplayTimeout: 6000, // 6 seconds
    });

    $('.school-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: true,
        items: 1,
        navText: ["<img src='/static/azeristudent/img/back.png'>", "<img src='/static/azeristudent/img/next.png'>"],
        autoplay: true,
        autoplayTimeout: 6000,
    });

    $('.dropdown').click(function () {
        if ($(this).hasClass('is-active')) {
            $(this).removeClass('is-active');
            $('.programs-menu').removeClass('show-countries');
            $('.overlay').removeClass('is-show');
        } else {
            $(this).addClass('is-active');
            $('.programs-menu').addClass('show-countries');
            $('.overlay').addClass('is-show');
        }
    });

    $('.overlay').click(function () {
        $('.dropdown').removeClass('is-active');
        $('.programs-menu').removeClass('show-countries');
        $('.overlay').removeClass('is-show');
    });

    $('.event-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        dots: false,
        navText: [
            "<img src='/static/azeristudent/img/back.png'>", "<img src='/static/azeristudent/img/next.png'>"
        ],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 3
            }
        }
    });

    $('.mobile-menu-btn').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
            $('.header-menu-mobile').hide();
        } else {
            $(this).addClass('active');
            $('.header-menu-mobile').show();
        }
    });

    function modalAnim(x) {
        $('.modal .modal-dialog').attr('class', 'modal-dialog  ' + x + '  animated');
    }

    $('#myModal').on('show.bs.modal', function (e) {
        modalAnim('bounceIn');
    });
    $('#myModal').on('hide.bs.modal', function (e) {
        modalAnim('bounceOut');
    });

    $(document).on("click", "#exhibition .acc_header", function () {
        var acc_header = $(this);
        var acc_body = acc_header.next();
        $("#exhibition .acc_header").not(acc_header).removeClass("active");
        acc_header.toggleClass("active");
        $("#exhibition .acc_body").not(acc_body).slideUp();
        acc_body.slideToggle();
    });

    // exhibition click scroller
    $(document).on("click", "#exhibition .participants .location", function (e) {
        e.preventDefault();
        var a = $(this);
        var id = a.data("location");
        var country_div = $("#exhibition").find("[data-id='" + id + "']");
        $("html, body").animate({scrollTop: country_div.offset().top});
    });
    // C A L E N D A R
    var reserveCalendar;
    reserveCalendar = new dhtmlXCalendarObject("calendar");
    reserveCalendar.hideTime();
    reserveCalendar.show();
    reserveCalendar.setHolidays("2019-03-08, 2019-03-20, 2019-03-21");
    reserveCalendar.setSensitiveRange(reserveCalendar.getDate(true), null);
    $(document).on('click', "#reserve #time button:not(.done):not(.disabled)", function (e) {
        var button = $(this);
        e.preventDefault();
        $("#reserve .register_popup").addClass("active");
        $("#reserve .register_popup #clock").text(button.siblings().filter("span").text());
        $("#reserve #input_clock").val(button.prev().text().split(":")[0]);
        if (button.is('#uni-reserve-btn')) {
            $("#reserve #input_clock").val(button.prev().text().split(":")[0]);
            $('#reserve .register_popup #reservation_form .add-option').show();
            $("#reserve #reservation_form .add-option select").removeAttr("disabled");

        } else if (button.is('#reserve-btn')) {
            $("#reserve #input_clock").val(button.prev().text().split(":")[0]);
            $('#reserve .register_popup #reservation_form .add-option').hide();
            $("#reserve #reservation_form .add-option select").attr("disabled", "disabled");
        }
    });

    $(document).on("click", "#reserve .register_popup #close_popup", function () {
        $("#reserve .register_popup").removeClass("active");
    });

    // $(document).on("click", "#reserve .register_popup form button", function(e){
    //   e.preventDefault();
    //   $("#reserve .mainRow").removeClass("active");
    //   $("#reserve .done_popup").addClass("active");
    // });

    if ($("#pasha_pg .videoHolder").length) {
        $("#pasha_pg .videoHolder .main_img").attr("src", "https://img.youtube.com/vi/" + $("#pasha_pg .videoHolder").data("url").split("=")[1].split("&")[0] + "/hqdefault.jpg");
    }

    $(document).on("click", "#pasha_pg .videoHolder", function () {
        var videoHolder = $(this);
        var url = videoHolder.data("url").split("=")[1].split("&")[0];
        url = "https://www.youtube.com/embed/" + url;

        $("#pasha_modal").find("iframe").attr("src", url);
        $("#pasha_modal").addClass("active");
    });

    $(document).on("click", "#pasha_modal .layout", function () {
        $("#pasha_modal").removeClass("active");
        $("#pasha_modal").find("iframe").attr("src", "");
    });

    moment.updateLocale('en', {
        // WEEK
        weekdaysMin: ["B", "Be", "Ça", "Ç", "Ca", "C", "Ş"],
        week: {dow: 1},

        // MONTH
        months: ["Yanvar", "Fevral", "Mart", "Aprel", "May", "İyun", "İyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"],
        monthsShort: ["Yan", "Fev", "Mar", "Apr", "May", "İyn", "İyl", "Avg", "Sen", "Okt", "Noy", "Dek"]
    });

    $('#birthday_input, #start_date_input, #end_date_input').datetimepicker({
        format: 'DD/MM/YYYY'
    });

    $('.bootstrap-datetimepicker-widget .prev').html('<i class="fa fa-chevron-left"></i>');
    $('.bootstrap-datetimepicker-widget .next').html('<i class="fa fa-chevron-right"></i>');

    var monthArray = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"];

    function make_date(date) {
        var day = date.getDate();
        var month = date.getMonth() + Number(1);
        var year = date.getFullYear();
        return year + "/" + month + "/" + day;
    }

    reserveCalendar.attachEvent("onClick", function (date) {
        var mydate = new Date(date);
        var monthIndex = mydate.getMonth();
        var senddate = make_date(mydate);
        var url = '/reserve/' + senddate + '/';
        var selected_date = mydate.getDate() + " " + monthArray[monthIndex] + " " + mydate.getFullYear();
        var selected_month_day = mydate.getDate() + " " + monthArray[monthIndex];

        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                $('.mainRow #time').html(data);
                $("#reserve .register_popup .selected_full_date").text(selected_date);
                $("#reserve .selected_month_day").text(selected_month_day);
                $('#reserve .register_popup .submit-after-url').val(url);
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            }
        });
    });


        // RESERVE POPUP FORM - UPDATING COUNTRIES FOR SELECTED EDUCATION CATEGORY
    $('#edu-category-selectbox').on('change', function () {
        var edu_category_id = $(this).children("option:selected").val();
        var url = '/reserve/country-universities/' + '?edu-cat=' + edu_category_id;

        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                $('#edu-cat-country-select').html(data);
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            }
        });
    });


    // RESERVE POPUP FORM - UPDATING EDUCATIONS FOR SELECTED COUNTRY
    $(document).on("change", "#edu-cat-country-selectbox", function () {
        var country_id = $(this).children("option:selected").val();
        var edu_cat_id = $(this).parentsUntil('.row').prev().find('#edu-category-selectbox').children("option:selected").val();
        console.log(edu_cat_id);

        var url = '/reserve/country-universities/' + '?country=' + country_id + '&edu-cat=' + edu_cat_id;

        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                $('#country-edu-select').html(data);
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            }
        });
    });

    $('#reservation_form').submit(function (e) {
        var data = $(this).serialize();
        // var base_form = $(this);
        var url = $('#reserve .register_popup .submit-after-url').val();
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            success: function (data) {
                if (data.save) {
                    // base_form.find("input[type=text], input[type=email]").val("");
                    $("#reserve .mainRow").removeClass("active");
                    window.location.href = "/done/";
                } else {
                    show_snackbar(data.message);
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            } // end error: function
        });
        return false;
    });

    // tab custom js
    $(".data-custom-tab h3").click(function (e) {
        $(".data-custom-tab h3").removeClass('active');
        $(this).addClass('active');
        $(".data-tab-item").hide();
        $($(this).data('href')).fadeIn();
    });

    $('.muraciet-button').click(function (e) {
        $(".base-title").text("Məsləhət lazımdırmı?");
    });

    // my custom js here
    if ($('section').is('.events')) {
        var url = window.location.href;
        $('.register-button').click(function (e) {

            if (window.location.href.includes("#qeydiyyat")) {
                $(".base-title").text("Qeydiyyat");
            }
            else {
                $(".base-title").text("Qeydiyyat");
                window.location.href += "#qeydiyyat";
            }
        });
        if (url.includes("#qeydiyyat")) {
            $('.register-button').click();
        }
    }


    $("#id_education_type").change(function (e) {
        e.preventDefault();
        var value = $(this).val();
        $.ajax({
            url: '/education/?value=' + value,
            type: "GET",
            processData: false,
            contentType: false,
            success: function (data) {
                // console.log(data);
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            } // end error: function
        });
    });

    if (divElement.is('.search-section')) {
        $.ajax({
            url: '/searchforms/',
            type: "GET",
            processData: false,
            contentType: false,
            success: function (data) {
                $('.search-section').html(
                    data
                );
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            } // end error: function
        });
    }
    if (divElement.is('.program-page')) {
        $(document).on("change", "#id_country", function (e) {
            var value = $('.education-search-form').attr('data-education_type');
            var country = $(this).val();
            if (value === "1") {
                // Ali mektebler
                $('.education-search-form').attr('action', '/countries/' + country + '/higher-education/');
            }
            else if (value === "2") {
                // Orta mektebler
                $('.education-search-form').attr('action', '/countries/' + country + '/secondary-education/');
            }
            else {
                // dil kurslari
                $('.education-search-form').attr('action', '/countries/' + country + '/language-program/');
            }
        });
        /*var search_url = "";
        if (window.country) {
            search_url = '/educationforms/?type=' + window.education_type + "&country=" + window.country;
        }
        else {
            search_url = '/educationforms/?type=' + window.education_type;
        }
        $.ajax({
            url: search_url,
            type: "GET",
            processData: false,
            contentType: false,
            success: function (data) {
                $('.education-search-form').html(
                    data
                );
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            } // end error: function
        });*/
    }

    $('#education-contact-form').submit(function (e) {
        var data = $(this).serialize();
        var base_form = $(this);
        $.ajax({
            url: '/contactform/',
            type: "POST",
            data: data,
            success: function (data) {
                if (data.save) {
                    base_form.find("input[type=text], input[type=email]").val("");
                    // show_snackbar("Tezliklə sizinlə əlaqə saxlanılacaq");
                    window.location.href = "/successful/";
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr, errmsg, err);
            } // end error: function
        });
        return false;
    });
    // if (divElement.is('.program-page')) {
    //     $(document).on('change', '#id_country', function (e) {
    //         var value = $(this).val();
    //         $.ajax({
    //             url: '/countrycity/?id=' + value,
    //             type: "GET",
    //             processData: false,
    //             contentType: false,
    //             success: function (data) {
    //                 $("#id_city").html(data);
    //             },
    //             error: function (xhr, errmsg, err) {
    //                 console.log(xhr, errmsg, err);
    //             } // end error: function
    //         });
    //     });
    // }
    // Contact us submit form
    $('.contact-submit-form').submit(function (e) {
        e.preventDefault();
        var base_form = $(this);
        var data = $(this).serialize();
        var url = $(this).data('action');
        var phone_valid = $(".phone-validation").attr("data-valid");
        // var email_valid = $(".email-validation").attr("data-valid");
        if (phone_valid === "true") {
            $.ajax({
                url: url,
                type: "POST",
                data: data,
                success: function (data) {
                    if (data.save) {
                        base_form.find("input[type=text], input[type=email], textarea").val("");
                        $('.close-btn').click();
                        window.location.href = "/successful/";
                    }
                    else {
                        show_snackbar(data.message.email[0]);
                    }
                },
                error: function (xhr, errmsg, err) {
                    console.log(xhr, errmsg, err);
                } // end error: function
            });
        }
        return false;
    });
    if (divElement.is('.search-section')) {
        $(document).on("change", "#id_education_type", function (e) {
            var value = $(this).val();
            var country = $("#id_country").val();
            if (value === "1") {
                // Ali mektebler
                $('#main-page-search-form').attr('action', '/countries/' + country + '/higher-education/');
            }
            else if (value === "2") {
                // Orta mektebler
                $('#main-page-search-form').attr('action', '/countries/' + country + '/secondary-education/');
            }
            else {
                // dil kurslari
                $('#main-page-search-form').attr('action', '/countries/' + country + '/language-program/');
            }
        });
        $(document).on("change", "#id_country", function (e) {
            var value = $('#id_education_type').val();
            var country = $(this).val();
            if (value === "1") {
                // Ali mektebler
                $('#main-page-search-form').attr('action', '/countries/' + country + '/higher-education/');
            }
            else if (value === "2") {
                // Orta mektebler
                $('#main-page-search-form').attr('action', '/countries/' + country + '/secondary-education/');
            }
            else {
                // dil kurslari
                $('#main-page-search-form').attr('action', '/countries/' + country + '/language-program/');
            }
        });
    }
    // main inputmask
    $(".mask-phone").inputmask({
        'mask': '999-99-99',
        "oncomplete": function () {
            $(".phone-validation").attr("data-valid", "true");
            $(".phone-err").text("");
        },
        "onincomplete": function () {
            $(".phone-validation").attr("data-valid", "false");
            $(".phone-err").text("Nömrə düzgün deyil*");
        },
        'autoUnmask': false
    });
    // $(".mask-email").inputmask({'alias': 'email',
    //     "oncomplete": function () {
    //         $(".email-validation").attr("data-valid", "true");
    //         $(".email-err").text("");
    //     },
    //     "onincomplete": function () {
    //         $(".email-validation").attr("data-valid", "false");
    //         $(".email-err").text("Email düzgün deyil*");
    //     },
    //     'autoUnmask': false
    // });

});
    // Register us submit form
    $('.register-submit-form').submit(function (event) {
        event.preventDefault();
        var base_form = $(this);
        var data = $(this).serialize();
        var url = $(this).data('action');
        var phone_valid = $(".phone-validation").attr("data-valid");
        // var email_valid = $(".email-validation").attr("data-valid");
        if (phone_valid === "true") {
            $.ajax({
                url: url,
                type: "POST",
                data: data,
                success: function (data) {
                    if (data.save) {
                        base_form.find("input[type=text], input[type=email], textarea").val("");
                        $('.close-btn').click();
                        window.location.href = "/successful/";
                    }
                    else {
                        show_snackbar(data.message.email[0]);
                    }
                },
                error: function (xhr, errmsg, err) {
                    console.log(xhr, errmsg, err);
                } // end error: function
            });
        }
        return false;
    });

