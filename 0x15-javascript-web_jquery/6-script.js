$('DIV#update_header').click(function () {
  $('header').text(function (index, text) {
    return text.replace('First HTML page', 'New Header!!!');
  });
});
