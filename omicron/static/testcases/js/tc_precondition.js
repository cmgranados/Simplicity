$( document ).ready(function() {
	var $lastChar =1, $newRow;
	var $descriptionType = 'Descripción';
	var $testCaseType = 'Caso de Prueba';
	var $descriptionTypeID = 'DES';
	var $testCaseTypeID = 'TST';
	
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
                error.appendTo('#errors');
            }
		};
	
    $.validator.addMethod('validateRepeatElements', function(value, ele) {
    	$valid = true;
    	$('#preconditionTable  > tbody  > tr').each(function (index) {
    		$selectedId = value;
			$addedId = $("input[type='hidden'][name^='preconditionTestCase_id']",this).val();
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

	
	$("#prec-description-form").validate();
	$("#test-cases-form").validate(CONF_VALIDATION);
	
	$( "#preconditionsModal #search-preconditions-btn" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/omicron/testcases/search",
	        data: { 
	            'q' : $('#q').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: searchSuccess,
	        dataType: 'html'
	    });
	});
	
	$( "#prec-add-description-row-btn" ).click(function(event) {
		event.preventDefault();
		jQuery( '#home' ).wrap( '<form id="prec-description-form" role="form" />' );
		$("#prec-description-form").validate();
		if($("#prec-description-form").valid()) {
			var $description = $('#prec_description_textarea').val();
			$firstRow = "<tr> \
	            <td><input type='checkbox' name='preconditionCheckbox' value='' class='require-one'></td> \
	            <td><span name='preconditionDescription_txt' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
	            <td><span name='preconditionType_txt' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
	            <input type='hidden' name='preconditionDescription' value='"+$description+"'></input> \
	            <input type='hidden' name='preconditionType' value='"+$descriptionTypeID+"'></input> \
	            </tr>"
				$('#preconditionTable tbody').append($firstRow)
		    $('#preconditionsModal').modal('hide');
		}
		jQuery( '#home' ).unwrap();
		  
	});
	
	$( "#prec-test-cases-form" ).submit(function(event) {
		event.preventDefault();
		$("#test-cases-form").validate(CONF_VALIDATION);
		if($("#test-cases-form").valid()) {
			$('#preconditionResultTable input:checkbox:checked').parents("tr").each(function (index) {
				$firstRow = "<tr> \
		            <td><input type='checkbox' name='preconditionCheckbox' value=''></td> \
		            <td><span name='preconditionDescription_txt' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[id=testCaseCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=testCaseNameRetrieved]').val()+"</span></td> \
		            <td><span name='preconditionType_txt' maxlength='11' readonly='readonly'>"+$testCaseType+"</span></td> \
		            <input type='hidden' name='preconditionDescription' value='"+$(this).find('input:hidden[id=testCaseCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=testCaseNameRetrieved]').val()+"'></input> \
		            <input type='hidden' name='preconditionType' value='"+$testCaseTypeID+"'></input> \
		            <input type='hidden' name='preconditionTestCase_id' value='"+$(this).find('input:hidden[id=testCaseIdRetrieved]').val()+"'></input> \
		        </tr>"
		        $('#preconditionTable tbody').append($firstRow)
				$('#preconditionsModal').modal('hide');
			});
		}
	});
			
	$( "#delete-precondition-row-btn" ).click(function() {
		$('input:checkbox:checked').parents("tr").remove();
	});
	
	$('#close-precondition-modal-btn').click(function(e) {
		$('#preconditionsModal').modal('hide')
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	$('#preconditionResultTable tbody').html(data);
}   
