	$( document ).ready(function() {
		$.fn.wizard.logging = true;
		var wizard = $('#satellite-wizard').wizard({
			keyboard : false,
						contentHeight : 400,
						contentWidth : 1000,
						backdrop: 'static'
		});
					
		$('#new-requirement-btn').click(function(e) {
							e.preventDefault();
							wizard.show();
						});

		$('#close-precondition-modal-btn').click(function(e) {
							$('#myModal').modal('hide')
						});
	});

