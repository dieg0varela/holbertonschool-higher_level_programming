window.onload = function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus, jqXHR) {
    $('DIV#hello').text(data.hello);
  });
};
