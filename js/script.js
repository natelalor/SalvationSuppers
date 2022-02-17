
//window.addEventListener('load', image_transition);
$("#submitButton").on("click", form_click);
$("#zero_gravity").on("mouseover", show_sponsor_name)
$("#brio_coffee").on("mouseover", show_sponsor_name)
$("#single_pebble").on("mouseover", show_sponsor_name)

var i = 0;
setInterval(image_transition, 5000);
function image_transition() {
    if(i == 8){
        i = 0;
    }
    const images = ["images/salvation_pic_1.jpg", 
    "images/salvation_pic_2.png",
    "images/salvation_pic_3.jpg",
    "images/salvation_pic_4.jpg",
    "images/salvation_pic_5.jpg",
    "images/salvation_pic_6.jpg",
    "images/salvation_pic_7.jpg",
    "images/salvation_pic_8.png",
    "images/salvation_pic_9.png"];

    $("#rotating_food_pic").attr("src", images[i]);

    i++;

    
}

function form_click() {
    $("#sign_up").empty();
    $("#sign_up").addClass("submitted");
    $("#sign_up").append('<h2>Thank You!</h2><h3>We will contact you shortly.</h3><!--<img src="images/happiness.png" alt="smile face">-->');
}

function show_sponsor_name(){
    $(".zero_gravity_container>p").addClass("show_p")
}















