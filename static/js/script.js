
//window.addEventListener('load', image_transition);
$("#submitButton").on("click", form_click);
$("#zero_gravity").on("mouseover", show_sponsor_name)
$("#brio_coffee").on("mouseover", show_sponsor_name)
$("#single_pebble").on("mouseover", show_sponsor_name)
$("#slow_food").on("mouseover", show_sponsor_name)
$("#submitButton").on("click",save_form);

let first_name;
let last_name;
let email;
let phone;
let interests;

 $("#txtFirstName").on("focusout", function(){
    first_name = $(this).val();
});
$("#txtLastName").on("focusout", function(){
    last_name = $(this).val();
});
$("#txtEmail").on("focusout", function(){
    email = $(this).val();
});
$("#telPhoneNumber").on("focusout", function(){
    phone = $(this).val();
});
$("#txtInterest").on("focusout", function(){
    interests = $(this).val();
});
function save_form(){
    var form_array = [first_name, last_name, email, phone, interests];
    console.log(form_array);
    $.ajax({
        url: "/save_form",
        type: "post",
        data:{form:form_array},
        success: function(response) {
            console.log(response);
        }
    });
};
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
function form_click() {
    $("#sign_up").empty();
    $("#sign_up").addClass("submitted");
    $("#sign_up").append('<h2>Thank You!</h2><h3>We will contact you shortly.</h3><!--<img src="images/happiness.png" alt="smile face">-->');
}
//show sponsor
function show_sponsor_name(){
    $(".zero_gravity_container>p").addClass("show_p")
}
//add to number of meals donated




