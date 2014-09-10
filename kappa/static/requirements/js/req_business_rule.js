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
			$addedId = $("input[type='hidden'][name^='businessruleId_']",this).val();
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


	function searchSuccessBr(data, textStatus, jqXHR) {
		$('#businessruleResultTable tbody').html(data);
	} 
	
	$( "#add-business-rule-row-btn" ).click(function() {
		if($("#br-form").valid()) {
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
		}
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
});
