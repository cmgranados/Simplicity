$(document).ready(function() {
	
	$("#save-testcase-btn").click(function(event){
		if($("#testCaseForm").valid()) {
			var testCase = buildTestCaseDefinion();
			buildTestCasePreconditions(testCase);
			buildTestCaseRequirements(testCase);
			buildTestCaseInputs(testCase);
			buildTestCaseProcedure(testCase);
			buildTestCasePostconditions(testCase);
			console.log('tc'+ JSON.stringify(testCase));
			$.ajax({
		        type: "POST",
		        url: "/omicron/save_testcase_ajax/",
		        data: { 
		            'testCase' : JSON.stringify(testCase),
		            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		        },
		        success: successTestCaseCreation,
		        dataType: 'html'
		    });
		}
	});
	
	function buildTestCaseDefinion() {
		var testcase = new Object();
		if( $('#testcaseID').val() != null && $('#testcaseID').val() != ""){
			testcase.test_case_id = $('#testcaseID').val();
		}else{
			testcase.test_case_id = 0;
		}
		testcase.name = $('#testCaseTitle').val();
		testcase.type = $('#testCaseType').val();
		testcase.description = $('#testCaseDescription').val();
		return testcase;
	}
	
	function buildTestCasePreconditions(testcase) {
			var list = [];
			var i = 0;
			$('#preconditionTable > tbody  > tr').each(function(index) {
				var precondition = new Object();
				var preconditionType = $("input[type='hidden'][name^='preconditionType']",this);
				var preconditionId = $("input[type='hidden'][name^='preconditionTestCase_id']",this);
				var descriptionId = $("input[type='hidden'][name^='preconditionDescription']",this);
				precondition.type = preconditionType.val();
				precondition.precondition_id = preconditionId.val();
				precondition.description = descriptionId.val();
				console.log(precondition.type); 
				console.log(precondition.id); 
				list[i] = precondition;
				i++;
			});
			testcase.preconditions = list;
	}
	
	function buildTestCaseRequirements(testcase) {
		var requirements = [];
		var i = 0;
		
		$('#requirementsTable > tbody  > tr').each(function(index) {
			var requirement = new Object();
			var id = $("input[type='hidden'][name^='requirementId']",this);
			requirement.id = id.val();
			console.log(requirement.id); 
			requirements[i] = requirement;
			i++;
		});
		testcase.requirements = requirements;
	}
	
	function buildTestCaseInputs(testcase) {
		var inputParameters = [];
		var i = 0;
		
		$('#tableInputParams > tbody  > tr').each(function(index) {
			var inputName = $(this).find("td").eq(1).find("input").val();
			var inputDescription = $(this).find("td").eq(2).find("input").val();
			var inputDataType = $(this).find("td").eq(3).find("select").val();
			
			var input = new Object();
			input.value = inputName;
			input.description = inputDescription;
			input.dataType = inputDataType;

			inputParameters[i] = input;
			i++;
		});
		
		testcase.inputParameters = inputParameters;
	}
	
	function buildTestCaseProcedure(testcase) {
		var procedureSteps = [];
		var i = 0;
		
		$('#tableProcess > tbody  > tr').each(function(index) {
			var stepNumber = $(this).find("td").eq(1).find("input").val();
			var stepActivity = $(this).find("td").eq(2).find("input").val();
			var step = new Object();
			step.value = stepNumber;
			step.activity = stepActivity;

			procedureSteps[i] = step;
			i++;
		});
		
		testcase.procedureSteps = procedureSteps;
	}
	
	function buildTestCasePostconditions(testcase) {
		var list = [];
		var i = 0;
		$('#postconditionTable > tbody  > tr').each(function(index) {
			var postcondition = new Object();
			var postconditionType = $("input[type='hidden'][name^='postconditionType']",this);
			var postconditionId = $("input[type='hidden'][name^='postconditionTestCase_id']",this);
			var descriptionId = $("input[type='hidden'][name^='postconditionDescription']",this);
			postcondition.type = postconditionType.val();
			postcondition.postcondition_id = postconditionId.val();
			postcondition.description = descriptionId.val();
			console.log(postcondition.type); 
			console.log(postcondition.id); 
			list[i] = postcondition;
			i++;
		});
		testcase.postconditions = list;
	}
	
	function successTestCaseCreation(data, textStatus, jqXHR) {
		$('#information-modal-tc').html(data);
		$('#modal-response-tc').modal('show');
	}  
	
	function failure(data, textStatus, jqXHR) {
		$('#information-modal-tc').html(data);
		$('#modal-response-tc').modal('show');
	}  
});
