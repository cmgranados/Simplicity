$(document).ready(function() {
	$('#rootwizard').bootstrapWizard({
		onNext : function(tab, navigation, index) {
			
			var isValid = validate(index);
			
			if(!isValid) {
				return false;
			}
		},
		onTabShow : function(tab, navigation, index) {
			var $total = navigation.find('li').length;
			var $current = index + 1;
			var $percent = ($current / $total) * 100;
			$( "#rootwizard" ).find('#bar').attr("aria-valuenow", $percent);
			$('#rootwizard').find('#bar').css({
				width : $percent + '%'
			});
		},
		
		onTabClick: function(tab, navigation, index) {
			/*var isValid = validate(index + 1);
			
			if(!isValid) {
				return false;
			}*/
			return false;
		}
	});
});