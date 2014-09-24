$( document ).ready(function() {
	var $lastChar =1, $newRow;
	var $descriptionType = 'Descripción';
	var $testCaseType = 'Caso de Prueba';
	var $descriptionTypeID = 'DES';
	var $testCaseTypeID = 'TST';
	
	var CONF_VALIDATION = {
			rules: {
				postcondition_checkbox: {
					onecheck: true,
					validateRepeatElements: true
				}
			},
			messages: {
			},
			errorPlacement: function(error, element) {
                error.appendTo('#errors');
            }
		};
	
    $.validator.addMethod('validateRepeatElements', function(value, ele) {
    	$valid = true;
    	$('#postconditionTable  > tbody  > tr').each(function (index) {
    		$selectedId = value;
			$addedId = $("input[type='hidden'][name^='postconditionTestCase_id']",this).val();
    		console.log("added: " + $selectedId + " lista: " + $addedId);
    		
    		if($selectedId == $addedId) {
    			$valid = false;
    			return false;
    		} else {
    			$valid = true;
    		}
    	});
    	
        return $valid;
    }, 'Alguno de los elementos seleccionados ya fue agregado como postcondición');
    
	$.validator.addMethod('onecheck', function(value, ele) {
        return $("input:checked").length >= 1;
    }, 'Debe seleccionar al menos un elemento de la lista');

	
	$("#post-description-form").validate();
	$("#test-cases-form").validate(CONF_VALIDATION);
	
	$( "#postconditionsModal #search-postconditions-btn" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/kappa/preconditions_ajax_search/",
	        data: { 
	            'q' : $('#q').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: searchSuccess,
	        dataType: 'html'
	    });
	});
	
	$( "#post-add-description-row-btn" ).click(function(event) {
		event.preventDefault();
		jQuery( '#home' ).wrap( '<form id="post-description-form" role="form" />' );
		$("#post-description-form").validate();
		if($("#post-description-form").valid()) {
			var $description = $('#post_description_textarea').val();
			$firstRow = "<tr> \
	            <td><input type='checkbox' name='postconditionCheckbox' value='' class='require-one'></td> \
	            <td><span name='postconditionDescription_txt' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
	            <td><span name='postconditionType_txt' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
	            <input type='hidden' name='postconditionDescription' value='"+$description+"'></input> \
	            <input type='hidden' name='postconditionType' value='"+$descriptionTypeID+"'></input> \
	            </tr>"
				$('#postconditionTable tbody').append($firstRow)
		    $('#postconditionsModal').modal('hide');
		}
		jQuery( '#home' ).unwrap();
		  
	});
	
	$( "#post-test-cases-form" ).submit(function(event) {
		event.preventDefault();
		$("#test-cases-form").validate(CONF_VALIDATION);
		if($("#test-cases-form").valid()) {
			$('#postconditionResultTable input:checkbox:checked').parents("tr").each(function (index) {
				$firstRow = "<tr> \
		            <td><input type='checkbox' name='postconditionCheckbox' value=''></td> \
		            <td><span name='postconditionDescription_txt' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[id=testCaseCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=testCaseTitleRetrieved]').val()+"</span></td> \
		            <td><span name='postconditionType_txt' maxlength='11' readonly='readonly'>"+$testCaseType+"</span></td> \
		            <input type='hidden' name='postconditionDescription' value='"+$(this).find('input:hidden[id=testCaseCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=testCaseNameRetrieved]').val()+"'></input> \
		            <input type='hidden' name='postconditionType' value='"+$testCaseTypeID+"'></input> \
		            <input type='hidden' name='postconditionTestCase_id' value='"+$(this).find('input:hidden[id=testCaseIdRetrieved]').val()+"'></input> \
		        </tr>"
		        $('#postconditionTable tbody').append($firstRow)
				$('#postconditionsModal').modal('hide');
			});
		}
	});
			
	$( "#delete-postcondition-row-btn" ).click(function() {
		$('input:checkbox:checked').parents("tr").remove();
	});
	
	$('#close-postcondition-modal-btn').click(function(e) {
		$('#postconditionsModal').modal('hide')
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	$('#postconditionResultTable tbody').html(data);
}   
