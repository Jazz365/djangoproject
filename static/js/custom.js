$(document).ready(function() {
   $(window).scroll(function(e) {  
    if ($(this).scrollTop() > 430) { 
      $('.box-wrapper').addClass("column");
    } else {
      $('.box-wrapper').removeClass("column");
    } 
  });     

  });

 