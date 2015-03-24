$(function() {

	var container = $('#table_container');

	// previous button click on table
	$('#prev_page_button').off('click.page').on('click.page', function() {
		var page = parseInt(container.data('page'));
		container.data('page', Math.max(0, page-1));
		container.trigger('table_refresh');
	});//click

	// next button click on table
	$('#next_page_button').off('click.page').on('click.page', function() {
		var page = parseInt(container.data('page'));
		container.data('page', page+1);
		container.trigger('table_refresh');
	});//click

	// handler to refresh the table
	container.on('table_refresh', function() {
		
		$.ajax({
			url: '/homepage/tabledemo.get_table/',
			data: {
				table_page: container.data('page'),
			},
		}).success(function(data) {
			container.html(data);
		});//ajax

	}).trigger('table_refresh');

});