$(function(){
	$('a.complete').click(function(){
		var elem = $(this).parents('.task');
		$.ajax({
			url: '/task/complete',
			type: 'UPDATE',
			data: '{"id": "'+elem.attr('data-id')+'"}',
			dataType: 'json',
			contentType: 'application/json; charset=utf-8',
			success: function(result, data){
				elem.fadeOut(500);
			}
		});
	});
	$('#save-task').click(function(){
		var data = {};
		data['name'] = $('.form-field[data-attribute="name"]').text();
		data['description'] = $('.form-field[data-attribute="description"]').text();
		$.ajax({
			url: '/task',
			type: 'PUT',
			data: JSON.stringify(data),
			dataType: 'json',
			contentType: 'application/json; charset=utf-8',
			success: function(result, data){
				$('#myModal').modal('hide');
				//add the new element, SON

				//elem.fadeOut(500);
			}
		});
	});
});

