$(document).ready(function() {
	
	$("#save-requirement-btn").click(function(){
		var requirement = buildRequirementDefinion();
		buildRequirementPreconditions(requirement);
		console.log('req'+ JSON.stringify(requirement));
		$.ajax({
	        type: "POST",
	        url: "/kappa/save_requirement_ajax/",
	        data: { 
	            'requirement' : JSON.stringify(requirement),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: success,
	        dataType: 'html'
	    });
	});
	
	
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
	
	function buildRequirementDefinion() {
		var requirement = new Object();
		requirement.name = $('#requirementTitle').val();
		requirement.code = $('#requirementCode').val();
		requirement.type = $('#requirementType').val();
		requirement.description = $('#requirementDescription').val();
		requirement.keywords = $('#requirementKeywords').val();
		return requirement;
	}
	
	function buildRequirementPreconditions(requirement) {
			var list = [];
			var i = 0;
			$('#preconditionTable > tbody  > tr').each(function(index) {
				var precondition = new Object();
				var preconditionType = $("input[type='hidden'][name^='preconditionType_']",this);
				var preconditionId = $("input[type='hidden'][name^='preconditionRequirement_id_']",this);
				var descriptionId = $("input[type='hidden'][name^='preconditionDescription_']",this);
				precondition.type = preconditionType.val();
				precondition.id = preconditionId.val();
				precondition.description = descriptionId.val();
				console.log(precondition.type); 
				console.log(precondition.id); 
				list[i] = precondition;
				i++;
			});
			requirement.preconditions = list;
	}
	
	function success() {
		alert("Done!!");
	}  
});

