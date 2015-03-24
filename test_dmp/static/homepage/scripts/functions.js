/**
 * Created by justin on 2/5/15.
 */

if( !$('#not-empty').is(':empty') ) {
    $('.alert').addClass('show');
}

jQuery("document").ready(function($){

	var left_menu = $('#main_left_content_menu');

	$(window).scroll(function () {
		if ($(this).scrollTop() > 250 && $(window).width() > 480) {
			left_menu.addClass("fixed");
		} else {
			left_menu.removeClass("fixed");
		}
	});
});