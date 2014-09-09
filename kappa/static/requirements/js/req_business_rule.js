$( document ).ready(function() {
	
	$('#brModal  #close-precondition-modal-btn').click(function(e) {
		$('#brModal').modal('hide')
	});
	
	$('#newRequirementModal  #close-precondition-modal-btn').click(function(e) {
		$('#brModal').modal('hide')
	});
	
	var $lastChar =1, $newRow;
	
	$( "#search-business-rules-btn" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/kappa/businessrules_ajax_search/",
	        data: { 
	            'br' : $('#br').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: searchSuccessBr,
	        dataType: 'html'
	    });
	});
	
	$get_lastID_br = function(obj){
	    var id = $('#businessrulesTable tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	        <td><input type='checkbox' name='businessruleCheckbox_"+$lastChar+"' value=''></td> \
	        <td><span name='businessruleName_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$(obj).find('input:hidden[name=businessRuleNameRetrieved]').val()+"</span></td> \
	        <td><span name='businessruleDescription_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$(obj).find('input:hidden[name=businessRuleDescriptionRetrieved]').val()+"</span></td> \
	        <input type='hidden' name='businessruleId_"+$lastChar+"' value='"+$(obj).find('input:hidden[name=businessRuleIdRetrieved]').val()+"'></input> \
	    </tr>"
	 return $newRow;
	}


	function searchSuccessBr(data, textStatus, jqXHR)
	{
	$('#businessruleResultTable tbody').append(data);
	} 
	
	$( "#add-business-rule-row-btn" ).click(function() {
		$('#businessruleResultTable input:checkbox:checked').parents("tr").each(function (index) {
			if($('#businessrulesTable tbody tr') != null && $('#businessrulesTable tbody tr').length == 0){
				var $lastChar =1;
				$firstRow = "<tr> \
		            <td><input type='checkbox' name='businessruleCheckbox_1' value=''></td> \
		            <td><span name='businessruleName_1' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[name=businessRuleNameRetrieved]').val()+"</span></td> \
		            <td><span name='businessruleDescription_1' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[name=businessRuleDescriptionRetrieved]').val()+"</span></td> \
		            <input type='hidden' name='businessruleId_1' value='"+$(this).find('input:hidden[name=businessRuleIdRetrieved]').val()+"'></input> \
		        </tr>"
		            $('#businessrulesTable tbody').append($firstRow)
			} else {
				$get_lastID_br($(this));
				$('#businessrulesTable > tbody:last').append($newRow);
			}
		});
		 $('#brModal').modal('hide');
	});
	
	$( "#delete-busines-rule-row-add" ).click(function() {
		$('#businessrulesTable input:checkbox:checked').parents("tr").remove();
		if($('#businessrulesTable tbody tr').length > 0){
			$('#businessrulesTable > tbody  > tr').each(function(index) {
				var $currentPosition = index+1;
				$("input[type='checkbox'][name^='businessruleCheckbox_']").attr( "name", "businessruleCheckbox_"+$currentPosition);
				$( "span[name^='businessruleName_']", this).attr( "name", "businessruleName_"+$currentPosition);
				$( "span[name^='businessruleDescription_']", this).attr( "name", "businessruleDescription_"+$currentPosition);
				$( "input[type='hidden'][name^='businessruleId_']", this).attr( "name", "businessruleId_"+$currentPosition);
			});
		}
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
	alert("done");
	} 
});
