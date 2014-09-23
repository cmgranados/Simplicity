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
	
	$("#save-requirement-btn").click(function(event){
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
	
	function validate(index) {
		var isValid = true;
		if (index == 1) {
			$("#myReqForm").validate();
			if (!$('#myReqForm').valid()) {
				isValid = false;
			}
		} else if(index == 4) {
			if (!$('#inputs-form').valid() || !$('#outputs-form').valid()) {
				isValid = false;
			}
		} else if(index == 5) {
			if (!$('criteria-form').valid()) {
				isValid = false;
			}
		}
		return isValid;
	}
	
	function buildRequirementDefinion() {
		var requirement = new Object();
		if( $('#requirementID').val() != null && $('#requirementID').val() != ""){
			requirement.requirement_id = $('#requirementID').val();
		}else{
			requirement.requirement_id = 0;
		}
		requirement.name = $('#requirementTitle').val();
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
				var preconditionType = $("input[type='hidden'][name^='preconditionType']",this);
				var preconditionId = $("input[type='hidden'][name^='preconditionRequirement_id']",this);
				var descriptionId = $("input[type='hidden'][name^='preconditionDescription']",this);
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
			var id = $("input[type='hidden'][name^='businessruleId']",this);
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
			var description = $(this).find("td").eq(2).find("textArea").val();
			var dataType = $(this).find("td").eq(3).find("select").val();
			
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
			var description = $(this).find("td").eq(2).find("textArea").val();
			var dataType = $(this).find("td").eq(3).find("select").val();
			
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
	
	function success(data, textStatus, jqXHR) {
		$('#information-modal').html(data);
		$('#modal-response-req').modal('show');
	}  
	
	function failure(data, textStatus, jqXHR) {
		$('#information-modal').html(data);
		$('#modal-response-req').modal('show');
	}  
});

