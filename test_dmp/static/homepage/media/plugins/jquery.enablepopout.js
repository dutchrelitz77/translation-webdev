/*
Description:  This is a popout for pictures
Author:  Justin R

How to use it:

- wrap your images in an <a><img> tag and put a <p> after the <a> tag to show
  the description of the picture
- Reference the plugin in your base template
- Reference the jQuery plugin for your specific gallery icons in your JS file

Example:

<div class="photos">          
	% for image in images:
        <a href="/static/images/${ image.imageSource }" download><img class="gallery-icon" src = "/static/images/${ image.imageSource }"></a>
        <p class="picture-title hidden">${ image.title }</p>
    % endfor
</div>


// This should showup in the javascript file to enable popout for the gallery icon
$('.gallery-icon').enablePopOut();

*/

(function($) {

	$.fn.enablePopOut = function() {

		//Start of hover function for popout
		this.hover(function() {
				$(this).stop().animate({
					height: "250px",
					width: "250px",
					top: "-10px",
					left: "-10px",
				}, 200);
				$(this).parent().next().removeClass("hidden");
			}, function() {
				$(this).stop().animate({
					height: "200px",
					width: "200px",
					top: "0px",
					left: "0px"
			}, 200);
				$(this).parent().next().addClass("hidden");
		});//hover function to enable popout

	};//end of function

})(jQuery);