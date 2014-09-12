$( document ).ready(function() {
	var $lastChar =1, $newRow;
	var $descriptionType = 'Descripción';
	var $requirementType = 'Requisito';
	var $descriptionTypeID = 'DES';
	var $requirementTypeID = 'REQ';
	
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
			$addedId = $("input[type='hidden'][name^='preconditionRequirement_id']",this).val();
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

	
	$("#description-form").validate();
	$("#requirements-form").validate(CONF_VALIDATION);
	
	$( "#myModal #search-preconditions-btn" ).click(function() {
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
	
	$( "#add-description-row-btn" ).click(function(event) {
		event.preventDefault();
		jQuery( '#home' ).wrap( '<form id="description-form" role="form" />' );
		$("#description-form").validate();
		if($("#description-form").valid()) {
			var $description = $('#description_textarea').val();
			$firstRow = "<tr> \
	            <td><input type='checkbox' name='preconditionCheckbox' value='' class='require-one'></td> \
	            <td><span name='preconditionDescription_txt' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
	            <td><span name='preconditionType_txt' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
	            <input type='hidden' name='preconditionDescription' value='"+$description+"'></input> \
	            <input type='hidden' name='preconditionType' value='"+$descriptionTypeID+"'></input> \
	            </tr>"
				$('#preconditionTable tbody').append($firstRow)
		    $('#myModal').modal('hide');
		}
		jQuery( '#home' ).unwrap();
		  
	});
	
	$( "#requirements-form" ).submit(function(event) {
		event.preventDefault();
		$("#requirements-form").validate(CONF_VALIDATION);
		if($("#requirements-form").valid()) {
			$('#preconditionResultTable input:checkbox:checked').parents("tr").each(function (index) {
				$firstRow = "<tr> \
		            <td><input type='checkbox' name='preconditionCheckbox' value=''></td> \
		            <td><span name='preconditionDescription_txt' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[id=requirementCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=requirementTitleRetrieved]').val()+"</span></td> \
		            <td><span name='preconditionType_txt' maxlength='11' readonly='readonly'>"+$requirementType+"</span></td> \
		            <input type='hidden' name='preconditionDescription' value='"+$(this).find('input:hidden[id=requirementCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=requirementTitleRetrieved]').val()+"'></input> \
		            <input type='hidden' name='preconditionType' value='"+$requirementTypeID+"'></input> \
		            <input type='hidden' name='preconditionRequirement_id' value='"+$(this).find('input:hidden[id=requirementIdRetrieved]').val()+"'></input> \
		        </tr>"
		        $('#preconditionTable tbody').append($firstRow)
				$('#myModal').modal('hide');
			});
		}
	});
			
	$( "#delete-precondition-row-btn" ).click(function() {
		$('input:checkbox:checked').parents("tr").remove();
	});
	
	$('#close-precondition-modal-btn').click(function(e) {
		$('#myModal').modal('hide')
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	$('#preconditionResultTable tbody').html(data);
}   
