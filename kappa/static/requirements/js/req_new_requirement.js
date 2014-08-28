$(document).ready(function() {

	$('.datepicker').datepicker({
		language : 'ES'
	});

	$('#rootwizard').bootstrapWizard({
		onNext : function(tab, navigation, index) {
			if (index == 1) {
				// Make sure we entered the name
				if (!$('#requirementTitle').val()) {
					alert('Debes ingresar un título');
					$('#name').focus();
					return false;
				}
			}

			// Set the name for the next tab
			$('#tab3').html('Hello, ' + $('#name').val());

		},
		onTabShow : function(tab, navigation, index) {
			var $total = navigation.find('li').length;
			var $current = index + 1;
			var $percent = ($current / $total) * 100;
			$('#rootwizard').find('.bar').css({
				width : $percent + '%'
			});
		}
	});
});
