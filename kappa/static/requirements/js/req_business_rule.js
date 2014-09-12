$( document ).ready(function() {
	
	var CONF_VALIDATION = {
			rules: {
				businessrule_checkbox: {
					onecheck: true,
					validate_repeat: true
				}
			},
			messages: {
			},
			errorPlacement: function(error, element) {
                error.appendTo('#errorsBr');
            }
		};
	
	$.validator.addMethod('onecheck', function(value, ele) {
        return $("input:checked").length >= 1;
    }, 'Debe seleccionar al menos un elemento de la lista')
    
    $.validator.addMethod('validate_repeat', function(value, ele) {
    	$valid = true;
    	$('#businessrulesTable  > tbody  > tr').each(function (index) {
    		$selectedId = value;
			$addedId = $("input[type='hidden'][name^='businessruleId']",this).val();
    		console.log("added: " + $selectedId + " lista: " + $addedId);
    		
    		if($selectedId == $addedId) {
    			$valid = false;
    			return false;
    		} else {
    			$valid = true;
    		}
    	});
    	
        return $valid;
    }, 'Alguno de los elementos seleccionados ya fue agregado')
	
	$('#brModal  #close-precondition-modal-btn').click(function(e) {
		$('#brModal').modal('hide')
	});
	
	$("#br-form").validate(CONF_VALIDATION);
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
	        dataType: 'html',
	        error: function(XMLHttpRequest, textStatus, errorThrown) { 
                alert("Hubo un error al intentar guardar la regla de negocio."); 
            }    
	    });
	});
	
	function searchSuccessBr(data, textStatus, jqXHR) {
		$('#businessruleResultTable tbody').html(data);
	} 
	
	$( "#add-business-rule-row-btn" ).click(function() {
		if($("#br-form").valid()) {
			$('#businessruleResultTable input:checkbox:checked').parents("tr").each(function (index) {
					var $lastChar =1;
					$firstRow = "<tr> \
			            <td><input type='checkbox' name='businessruleCheckbox' value=''></td> \
			            <td><span name='businessruleName' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[name=businessRuleNameRetrieved]').val()+"</span></td> \
			            <td><span name='businessruleDescription' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[name=businessRuleDescriptionRetrieved]').val()+"</span></td> \
			            <input type='hidden' name='businessruleId' value='"+$(this).find('input:hidden[name=businessRuleIdRetrieved]').val()+"'></input> \
			        </tr>"
			            $('#businessrulesTable tbody').append($firstRow)
			});
			 $('#brModal').modal('hide');
		}
	});
	
	$( "#delete-busines-rule-row-add" ).click(function() {
		$('#businessrulesTable input:checkbox:checked').parents("tr").remove();
	});
});
