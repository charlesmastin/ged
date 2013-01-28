$(function(){
	var capture = true;
	$(document).on('click', '.task a.complete', function(){
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
	$(document).on('click', '#new-task', function(){
		$('#task').modal('show');
		$('#task').removeClass('update');
		$('#task').addClass('put');
		$('#task .form-field[data-attribute="name"]').focus();
		capture = false;
		return false;
	});
	$(document).on('click', '.task .actions .edit', function(){
		var elem = $(this).parents('.task');
		// open modal, stuff the goods, bind the callback of action
		$('#task').modal('show');
		$('#task').removeClass('put');
		$('#task').addClass('update');
		$('#task').attr('data-id', elem.attr('data-id'));
		$('#task .form-field[data-attribute="name"]').val(elem.find('*[data-attribute="name"]').text());
		$('#task .form-field[data-attribute="description"]').text(elem.find('*[data-attribute="description"]').text());
		$('#task .form-field[data-attribute="due_date"]').val(elem.find('*[data-attribute="due_date"]').text());
		capture = false;
		return false;
	});
	$(document).on('click', '#task.put .submit', function(){
		var data = getTaskData();
		$.ajax({
			url: '/task',
			type: 'PUT',
			data: JSON.stringify(data),
			dataType: 'json',
			contentType: 'application/json; charset=utf-8',
			success: function(result, data){
				$('#task').modal('hide');
				//add the new element, SON

				//elem.fadeOut(500);
				window.location.reload();
			}
		});
	});
	$(document).on('click', '#task.update .submit', function(){
		var data = getTaskData();
		data['id'] = $('#task').attr('data-id');
		$.ajax({
			url: '/task',
			type: 'UPDATE',
			data: JSON.stringify(data),
			dataType: 'json',
			contentType: 'application/json; charset=utf-8',
			success: function(result, data){
				$('#task').modal('hide');
				//add the new element, SON

				//elem.fadeOut(500);
				window.location.reload();
			}
		});
	});
	$('#task').on('hidden', function(){
		capture = true;
	});
	$(document).on('keydown', function(event){
		if(capture){
			if(event.which == 76){
				$('section.tasks').removeClass('grid').addClass('list');
			}
			if(event.which == 71){
				$('section.tasks').removeClass('list').addClass('grid');
			}
			if(event.which == 78){
				$('#new-task').trigger('click');
			}
		}
	});
});

//* convert to a javascript date object? */
function getTaskData(){
	var data = {};
	data['name'] = $('#task .form-field[data-attribute="name"]').val();
	data['description'] = $('#task .form-field[data-attribute="description"]').val();
	data['due_date'] = $('#task .form-field[data-attribute="due_date"]').val();
	return data;
}

