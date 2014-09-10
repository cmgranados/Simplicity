$( document ).ready(function() {
	$("#newRequirementModal #close-precondition-modal-btn").click(function(e) {
		$('#newRequirementModal').modal('hide')
	});
	
	$( "#add-br-row-btn" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/kappa/new_businessrule_ajax/",
	        data: { 
	            'newBusinessRuleTitle' : $('#newBusinessRuleTitle').val(),
	            'newBusinessRuleCode' : $('#newBusinessRuleCode').val(),
	            'businessRulesType' : $('#businessRulesType').val(),
	            'newBusinessRuleDescription' : $('#newBusinessRuleDescription').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: saveSuccessBr,
	        dataType: 'html'
	    });
	});
	
	function saveSuccessBr(data, textStatus, jqXHR)
	{
	alert("Regla de negocio creada con éxito");
	$('#newRequirementModal').modal('hide')
	} 
});
