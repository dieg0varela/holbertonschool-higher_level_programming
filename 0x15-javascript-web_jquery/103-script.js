window.onload = function(){
    $("INPUT#btn_translate").click(function(){

        const lang = $("INPUT#language_code").val();
        $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${lang}`,function (data, textStatus, jqXHR) {
            $("DIV#hello").text(data.hello);
        });
    });

    $('INPUT#language_code').keypress(function (e) {
        var key = e.which;
        if(key == 13)
         {
           $('INPUT#btn_translate').click();
           return false;  
         }
       });
};