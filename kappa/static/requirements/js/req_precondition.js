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
					validate_repeat: true
				}
			},
			messages: {
			},
			errorPlacement: function(error, element) {
                error.appendTo('#errors');
            }
		};
	
	$.validator.addMethod('onecheck', function(value, ele) {
        return $("input:checked").length >= 1;
    }, 'Debe seleccionar al menos un elemento de la lista')
    
    $.validator.addMethod('validate_repeat', function(value, ele) {
    	$valid = true;
    	$('#preconditionTable  > tbody  > tr').each(function (index) {
    		$selectedId = value;
			$addedId = $("input[type='hidden'][name^='preconditionRequirement_id_']",this).val();
    		console.log("added: " + $selectedId + " lista: " + $addedId);
    		
    		if($selectedId == $addedId) {
    			$valid = false;
    			return false;
    		} else {
    			$valid = true;
    		}
    	});
    	
        return $valid;
    }, 'Alguno de los elementos seleccionados ya fue agregado como precondición')
	
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
			if($('#preconditionTable tbody tr').length == 0){
				var $lastChar =1;
				var $description = $('#description_textarea').val();
				$firstRow = "<tr> \
		            <td><input type='checkbox' name='preconditionCheckbox_1' value='' class='require-one'></td> \
		            <td><span name='preconditionPosition_txt_1' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
		            <td><span name='preconditionDescription_txt_1' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
		            <td><span name='preconditionType_txt_1' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
		            <input type='hidden' name='preconditionPosition_1' value='"+$lastChar+"'></input> \
		            <input type='hidden' name='preconditionDescription_1' value='"+$description+"'></input> \
		            <input type='hidden' name='preconditionType_1' value='"+$descriptionTypeID+"'></input> \
		            </tr>"
				$('#preconditionTable tbody').append($firstRow)
		    } else {
		    	$get_lastID_desc();
				$('#preconditionTable > tbody:last').append($newRow);
		    };
		    $('#myModal').modal('hide');
		}
		jQuery( '#home' ).unwrap();
		  
	});
	
	$( "#requirements-form" ).submit(function(event) {
		event.preventDefault();
		if($("#requirements-form").valid()) {
			$('#preconditionResultTable input:checkbox:checked').parents("tr").each(function (index) {
				if($('#preconditionTable tbody tr') != null && $('#preconditionTable tbody tr').length == 0){
					var $lastChar =1;
					$firstRow = "<tr> \
			            <td><input type='checkbox' name='preconditionCheckbox_1' value=''></td> \
			            <td><span name='preconditionPosition_txt_1' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
			            <td><span name='preconditionDescription_txt_1' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[id=requirementCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=requirementTitleRetrieved]').val()+"</span></td> \
			            <td><span name='preconditionType_txt_1' maxlength='11' readonly='readonly'>"+$requirementType+"</span></td> \
			            <input type='hidden' name='preconditionPosition_1' value='"+$(this).find('input:hidden[id=requirementIdRetrieved]').val()+"'></input> \
			            <input type='hidden' name='preconditionDescription_1' value='"+$(this).find('input:hidden[id=requirementCodeRetrieved]').val()+"-"+$(this).find('input:hidden[id=requirementTitleRetrieved]').val()+"'></input> \
			            <input type='hidden' name='preconditionType_1' value='"+$requirementTypeID+"'></input> \
			            <input type='hidden' name='preconditionRequirement_id_1' value='"+$(this).find('input:hidden[id=requirementIdRetrieved]').val()+"'></input> \
			        </tr>"
			        $('#preconditionTable tbody').append($firstRow)
				} else {
					$get_lastID_req($(this));
					$('#preconditionTable > tbody:last').append($newRow);
				}
				 $('#myModal').modal('hide');
			});
		}
	});
			
	
	$get_lastID_desc = function(){
	    var id = $('#preconditionTable tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    var  $description = $('#description_textarea').val();
	    $lastChar++;
	    $newRow = "<tr> \
            <td><input type='checkbox' name='preconditionCheckbox_"+$lastChar+"' value=''></td> \
            <td><span name='preconditionPosition_txt_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
            <td><span name='preconditionDescription_txt_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
            <td><span name='preconditionType_txt_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
            <input type='hidden' name='preconditionPosition_"+$lastChar+"' value='"+$lastChar+"'></input> \
		    <input type='hidden' name='preconditionDescription_"+$lastChar+"' value='"+$description+"'></input> \
		    <input type='hidden' name='preconditionType_"+$lastChar+"' value='"+$descriptionTypeID+"'></input> \
        </tr>"
     return $newRow;
	}
	
	$get_lastID_req = function(obj){
	    var id = $('#preconditionTable tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar++;
	    $newRow = "<tr> \
            <td><input type='checkbox' name='preconditionCheckbox_"+$lastChar+"' value=''></td> \
            <td><span name='preconditionPosition_txt_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
            <td><span name='preconditionDescription_txt_"+$lastChar+"' maxlength='11' readonly='readonly'>"+
            		$(obj).find('input:hidden[id=requirementCodeRetrieved]').val()+"-"+$(obj).find('input:hidden[id=requirementTitleRetrieved]').val()+
            	"</span></td> \
            <td><span name='preconditionType_txt_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$requirementType+"</span></td> \
            <input type='hidden' name='preconditionPosition_"+$lastChar+"' value='"+$lastChar+"'></input> \
		    <input type='hidden' name='preconditionDescription_"+$lastChar+"' value='"+$(obj).find('input:hidden[id=requirementCodeRetrieved]').val()+"-"+$(obj).find('input:hidden[id=requirementTitleRetrieved]').val()+"'></input> \
		    <input type='hidden' name='preconditionType_"+$lastChar+"' value='"+$requirementTypeID+"'></input> \
		    <input type='hidden' name='preconditionRequirement_id_"+$lastChar+"' value='"+$(obj).find('input:hidden[id=requirementIdRetrieved]').val()+"'></input> \
        </tr>"
     return $newRow;
	}

	$( "#delete-precondition-row-btn" ).click(function() {
		$('input:checkbox:checked').parents("tr").remove();
		if($('#preconditionTable tbody tr').length > 0){
			$('#preconditionTable > tbody  > tr').each(function(index) {
				var $currentPosition = index+1;
				$( "input[type='checkbox'][name^='preconditionCheckbox_']").attr( "name", "preconditionCheckbox_"+$currentPosition);
				$( "span[name^='preconditionPosition_txt_']", this).attr( "name", "preconditionPosition_txt_"+$currentPosition);
				$( "span[name^='preconditionDescription_txt_']", this).attr( "name", "preconditionDescription_txt_"+$currentPosition);
				$( "span[name^='preconditionType_txt_']", this).attr( "name", "preconditionType_txt_"+$currentPosition);
				$( "input[type='hidden'][name^='preconditionPosition_']", this).attr( "name", "preconditionPosition_"+$currentPosition);
				$( "input[type='hidden'][name^='preconditionDescription_']", this).attr( "name", "preconditionDescription_"+$currentPosition);
				$( "input[type='hidden'][name^='preconditionType_']", this).attr( "name", "preconditionType_"+$currentPosition);
				$( "input[type='hidden'][name^='preconditionRequirement_id_']", this).attr( "name", "preconditionRequirement_id_"+$currentPosition);
				$( "span[name^='preconditionPosition_txt_']", this).text($currentPosition);
			});
		}
	});
	
	$('#close-precondition-modal-btn').click(function(e) {
		$('#myModal').modal('hide')
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	$('#preconditionResultTable tbody').html(data);
}   
