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

function validateName(el) {
				var name = el.val();
				var retValue = {};

				if (name == "") {
					retValue.status = false;
					retValue.msg = "Por favor ingrese un nombre";
				} else {
					retValue.status = true;
				}

				return retValue;
			};

function validateName(el) {
				var name = el.val();
				var retValue = {};

				if (name == "") {
					retValue.status = false;
					retValue.msg = "Por favor ingrese un nombre";
				} else {
					retValue.status = true;
				}

				return retValue;
			};