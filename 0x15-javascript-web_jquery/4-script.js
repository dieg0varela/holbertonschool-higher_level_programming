$("DIV#toggle_header").click(function(){
    if ($("header").attr("class") == "green"){
        $("header").toggleClass("green red");
    } else {
        $("header").toggleClass("red green");
    }
});