$(document).ready(function() {
	var CONF_VALIDATION = {
		rules: {
			requirementTitle: {
				
			},
			requirementType: {
				required: true,
				selectcheck: true
			}
		},
		messages: {
			requirementType: {
				
			}
		}
	};
	
	jQuery.validator.addMethod('selectcheck', function (value) {
        return (value != 'default');
    }, "Este campo es obligatorio");
	
	
	$("#myReqForm").validate(CONF_VALIDATION);
	
	$("#myReqForm").submit(function(event){
		$("#myReqForm").validate(CONF_VALIDATION);
		event.preventDefault();
		
		if($("#myReqForm").valid()) {
			var requirement = buildRequirementDefinion();
			buildRequirementPreconditions(requirement);
			buildRequirementBusinessRules(requirement);
			buildOutputInformation(requirement);
			buildInputInformation(requirement);
			buildAcceptanceCriteria(requirement);
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
		}
	});
	
	
	$('.datepicker').datepicker({
		language : 'ES'
	});

	$('#rootwizard').bootstrapWizard({
		onNext : function(tab, navigation, index) {
			$("#myReqForm").validate();
			if (index == 1) {
				// Make sure we entered the name
				if (!$('#requirementTitle').valid()) {
					//alert('Debes ingresar un título');
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
		//requirement.code = $('#requirementCode').val();
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
	
	function buildRequirementBusinessRules(requirement) {
		var businessRules = [];
		var i = 0;
		
		$('#businessrulesTable > tbody  > tr').each(function(index) {
			var businessRule = new Object();
			var id = $("input[type='hidden'][name^='businessruleId_']",this);
			businessRule.id = id.val();
			console.log(businessRule.id); 
			businessRules[i] = businessRule;
			i++;
		});
		requirement.businessRules = businessRules;
	}
	
	function buildOutputInformation(requirement) {
		var inputInformation = [];
		var outputInformation = [];
		var i = 0;
		
		$('#outputTable > tbody  > tr').each(function(index) {
			var out = $(this).find("td").eq(1).find("input").val();
			var description = $(this).find("td").eq(2).find("input").val();
			var dataType = $(this).find("td").eq(3).find("input").val();
			
			var output = new Object();
			output.value = out;
			output.description = description;
			output.dataType = dataType;
		
			console.log(output.value); 
			outputInformation[i] = output;
			i++;
		});
		
		requirement.outputInformation = outputInformation;
	}
	
	function buildInputInformation(requirement) {
		var inputInformation = [];
		var i = 0;
		
		$('#inputTable > tbody  > tr').each(function(index) {
			var inp = $(this).find("td").eq(1).find("input").val();
			var description = $(this).find("td").eq(2).find("input").val();
			var dataType = $(this).find("td").eq(3).find("input").val();
			
			var input = new Object();
			input.value = inp;
			input.description = description;
			input.dataType = dataType;
		
			console.log(inp.value); 
			inputInformation[i] = input;
			i++;
		});
		
		requirement.inputInformation = inputInformation;
	}
	
	function buildAcceptanceCriteria(requirement) {
		var acceptanceCriteria = [];
		var i = 0;
		
		$('#tableCriteria > tbody  > tr').each(function(index) {
			var crit = $(this).find("td").eq(1).find("input").val();
			var description = $(this).find("td").eq(2).find("input").val();
			
			var criteria = new Object();
			criteria.value = crit;
			criteria.description = description;
		
			console.log(criteria.value); 
			acceptanceCriteria[i] = criteria;
			i++;
		});
		
		requirement.acceptanceCriteria = acceptanceCriteria;
	}
	
	function success() {
		alert("Done!!");
	}  
});

