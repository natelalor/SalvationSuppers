
$("#zero_gravity").on("mouseover", show_sponsor_name)
$("#brio_coffee").on("mouseover", show_sponsor_name)
$("#single_pebble").on("mouseover", show_sponsor_name)
$("#slow_food").on("mouseover", show_sponsor_name)
$(".admin_delete_volunteer").on("click", delete_volunteer)

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 44.47607, lng: -73.21685 },
    zoom: 16,
  });
  const marker = new google.maps.Marker({
    position: { lat: 44.47607, lng: -73.21685 },
    map: map,
  });

}

<<<<<<< HEAD
        var form_array = [first_name, last_name, email, phone, interests];
        $.ajax({
            url: "/save_form",
            type: "post",
            data:{form:form_array},
            success: function(response) {
                console.log(response);
            }
        });
    }
};
function display_volunteers(){
    $(".show_volunteer_container").remove();
=======
window.initMap = initMap;

function delete_volunteer(){
    let id = $(this).attr('id').substring(9,$(this).attr('id').length);
    let idData = [id]
>>>>>>> d3c97f9598026123033b16c934e18d3134cd4e59
    $.ajax({
        url: "/delete_volunteer",
        type: 'POST',
        data: {data: idData},
        success: function(response){
            console.log(response);
            location.reload();
        },
        error: function(error){
            console.log(error);
        }
    });
<<<<<<< HEAD
}
function save_header(){
    //save our header here

    $.ajax({
        url: "/save_header",
        type: "post",
        data:{header: header_text},
        success: function(response) {
            console.log(response);
        }
    });

}
function save_num_meals(){
    // save number of meals here
    $.ajax({
        url: "/save_num_meals",
        type: "post",
        data:{form:form_array},
        success: function(response) {
            console.log(response);
        }
    });
}
=======
};

>>>>>>> d3c97f9598026123033b16c934e18d3134cd4e59
//Image transition section
var i = 0;
setInterval(image_transition, 3200);
function image_transition() {
    if(i == 8){
        i = 0;
    }
    const images = ["../static/images/salvation_pic_1.jpg", 
    "../static/images/salvation_pic_2.png",
    "../static/images/salvation_pic_3.jpg",
    "../static/images/salvation_pic_4.jpg",
    "../static/images/salvation_pic_5.jpg",
    "../static/images/salvation_pic_6.jpg",
    "../static/images/salvation_pic_7.jpg",
    "../static/images/salvation_pic_8.png",
    "../static/images/salvation_pic_9.png"];

    $("#rotating_food_pic").attr("src", images[i]);

    i++;
    
}

//form submitted animation
/*function form_click() {
    $("#sign_up").empty();
    $("#sign_up").addClass("submitted");
    $("#sign_up").append('<h2>Thank You!</h2><h3>We will contact you shortly.</h3><!--<img src="images/happiness.png" alt="smile face">-->');
}*/
//show sponsor
function show_sponsor_name(){
    $(".zero_gravity_container>p").addClass("show_p")
}
//add to number of meals donated




