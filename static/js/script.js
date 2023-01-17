
//window.addEventListener('load', image_transition);
//$("#submitButton").on("click", form_click);
$("#zero_gravity").on("mouseover", show_sponsor_name)
$("#brio_coffee").on("mouseover", show_sponsor_name)
$("#single_pebble").on("mouseover", show_sponsor_name)
$("#slow_food").on("mouseover", show_sponsor_name)
$("#submitButton").on("click", save_form)
$("#show_volunteer_button").on("click", display_volunteers)

var regEx = /^[0-9a-zA-Z]+$/;
var email_validation = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
var phone_validation = /^\d{10}$/;

let first_name;
let last_name;
let email;
let phone;
let interests;
let able_to_save = true;

 $("#txtFirstName").on("focusout", function(){
    first_name = $(this).val();
    if(first_name.match(regEx)){
        able_to_save = true;
    }else{
        $("#sign_up").append("<p class='validation_message'>First name can only have letters</p>")
        able_to_save = false;
    }
});
$("#txtLastName").on("focusout", function(){
    last_name = $(this).val();
    if(last_name.match(regEx)){
        able_to_save = true;
    }else{
        $("#sign_up").append("<p class='validation_message'>Last name can only have letters</p>")
        able_to_save = false;
    }
});
$("#txtEmail").on("focusout", function(){
    email = $(this).val();
    if(email.match(email_validation)){
        able_to_save = true;
    }else{
        $("#sign_up").append("<p class='validation_message'>Email is missing some required characters</p>")
        able_to_save = false;
    }
});
$("#telPhoneNumber").on("focusout", function(){
    phone = $(this).val();
    /*if(phone.match(phone_validation)){
        able_to_save = true;
    }else{
        $("#sign_up").append("<p class='validation_message'>Phone numbers can only have numbers, (), and -</p>")
        able_to_save = false;
    }*/
});
$("#txtInterest").on("focusout", function(){
    interests = $(this).val();
    if(interests.match(regEx)){
        able_to_save = true;
    }
    else if(interests == ""){
        able_to_save = true;
    }else{
        $("#sign_up").append("<p class='validation_message'>Your \"interests\" has invalid characters</p>")
        able_to_save = false;
    }
});
function save_form(){
    if(able_to_save){
        $("#sign_up").empty();
        $("#sign_up").addClass("submitted");
        $("#sign_up").append('<h2>Thank You!</h2><h3>We will contact you shortly.</h3><!--<img src="images/happiness.png" alt="smile face">-->');

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
    }
};
function display_volunteers(){
    $(".show_volunteer_container").remove();
    $.ajax({
        url: "/display_volunteers",
        type: "post",
        success: function(response) {
            console.log(response);
            for(var i = 0; i < response.length; ++i){
                $(".table_wrapper").append("<div class = 'all_volunteers' id='volunteer_"+i+"'></div>")
                $("#volunteer_" + i).append("<p>"  +  response[i][0] + " " + response[i][1] + "</p>")
                $("#volunteer_" + i).append("<p>"  +  response[i][2] +"</p>")
                $("#volunteer_" + i).append("<p>"  +  response[i][3] +"</p>")
                $("#volunteer_" + i).append("<p>"  +  response[i][4] +"</p>")
            }
        }
    });
}
function save_header(){
    
}
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




