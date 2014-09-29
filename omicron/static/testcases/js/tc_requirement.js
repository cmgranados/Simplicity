$( document ).ready(function() {
	
	var CONF_VALIDATION = {
			rules: {
				precondition_checkbox: {
					onecheck: true,
					validateRepeatElements: true
				}
			},
			messages: {
			},
			errorPlacement: function(error, element) {
                error.appendTo('#errorsReqs');
            }
		};
	
	$.validator.addMethod('validateRepeatElements', function(value, ele) {
    	$valid = true;
    	$('#requirementsTable  > tbody  > tr').each(function (index) {
    		$selectedId = value;
			$addedId = $("input[type='hidden'][name^='requirementId']",this).val();
    		console.log("added: " + $selectedId + " lista: " + $addedId);
    		
    		if($selectedId == $addedId) {
    			$valid = false;
    			return false;
    		} else {
    			$valid = true;
    		}
    	});
    	
        return $valid;
    }, 'Alguno de los elementos seleccionados ya fue agregado como precondición');
    
	$.validator.addMethod('onecheck', function(value, ele) {
        return $("input:checked").length >= 1;
    }, 'Debe seleccionar al menos un elemento de la lista');

	
	$("#req-form").validate(CONF_VALIDATION);
	
	$('#reqModal  #close-requirement-modal-btn').click(function(e) {
		$('#reqModal').modal('hide')
	});
	
	$( "#reqModal #search-requirements-btn" ).click(function() {
			$.ajax({
		        type: "POST",
		        url: "/kappa/requirements_ajax_search/",
		        data: { 
		            'q' : $('#requirementSearchText').val(),
		            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		        },
		        success: searchSuccessReq,
		        dataType: 'html'
		    });
	});
	
	function searchSuccessReq(data, textStatus, jqXHR) {
		$('#requirementResultTable tbody').html(data);
	} 
	
	$( "#add-requirement-row-btn" ).click(function() {
		$("#req-form").validate(CONF_VALIDATION);
		if($("#req-form").valid()) {
			$('#requirementResultTable input:checkbox:checked').parents("tr").each(function (index) {
					var $lastChar =1;
					$firstRow = "<tr> \
			            <td><input type='checkbox' name='requirementeCheckbox' value=''></td> \
			            <td><span name='requirementName' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[id=requirementTitleRetrieved]').val()+"</span></td> \
			            <input type='hidden' name='requirementId' value='"+$(this).find('input:hidden[id=requirementIdRetrieved]').val()+"'></input> \
			        </tr>"
			            $('#requirementsTable tbody').append($firstRow)
			});
			 $('#reqModal').modal('hide');
		}
	});
	
	$( "#delete-requirement-rule-row-add" ).click(function() {
		$('#requirementsTable input:checkbox:checked').parents("tr").remove();
	});
});