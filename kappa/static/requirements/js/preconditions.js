$( document ).ready(function() {
	var $lastChar =1, $newRow;
	var $descriptionType = 'Descripción';
	
	$( "#searchPreconditions" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/search/",
	        data: { 
	            'q' : $('#q').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: searchSuccess,
	        dataType: 'html'
	    });
	});
	
	
	$( "#add_DescriptionRow" ).click(function() {
		if($('#precondition_table tbody tr').length == 0){
			var $lastChar =1;
			var $description = $('#description_textarea').val();
			$firstRow = "<tr> \
	            <td><input type='checkbox' name='precondition_checkbox_1' value=''></td> \
	            <td><span name='precondition_id_1' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
	            <td><span name='precondition_description_1' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
	            <td><span name='precondition_type_1' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
	        </tr>"
			$('#precondition_table tbody').append($firstRow)
			$firstRowHiddenId = "<input type='hidden' id='precondition_id_1_hidden' name='precondition_id_1_hidden' value='"+$lastChar+"'></input>"
			$firstRowHiddenDesc = "<input type='hidden' id='precondition_description_1_hidden' name='precondition_description_1_hidden' value='"+$description+"'></input>"
			$firstRowHiddenType = "<input type='hidden' id='precondition_id_1_hidden' name='precondition_id_1_hidden' value='"+$lastChar+"'></input>"
			$('#form_requirements').append($firstRowHiddenDesc)
			$('#form_requirements').append($firstRowHiddenId)
			$('#form_requirements').append($firstRowHiddenDesc)
	    } else {
	    	$get_lastID();
			$('#precondition_table > tbody:last').append($newRow);
	    };
	    $('#myModal').modal('hide');
		  
	});
	
	$get_lastID = function(){
	    var id = $('#precondition_table tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    var  $description = $('#description_textarea').val();
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
            <td><input type='checkbox' name='precondition_checkbox_"+$lastChar+"' value=''></td> \
            <td><span name='precondition_id_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
            <td><span name='precondition_description_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
            <td><span name='precondition_type_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
        </tr>"
     return $newRow;
	}

	$( "#delete_PreconditionRow" ).click(function() {
		$('input:checkbox:checked').parents("tr").remove();
		if($('#precondition_table tbody tr').length > 0){
			$('#precondition_table > tbody  > tr').each(function(index) {
				var $currentPosition = index+1;
				$( "input[id][name$='man']" ).val( "only this one" );
				$("input[type='checkbox'][name^='precondition_checkbox_']").attr( "name", "precondition_checkbox_"+$currentPosition);
				$( "span[name^='precondition_id_']", this).attr( "name", "precondition_id_"+$currentPosition);
				$( "span[name^='precondition_description_']", this).attr( "name", "precondition_description_"+$currentPosition);
				$( "span[name^='precondition_type_']", this).attr( "name", "precondition_type_"+$currentPosition);
				$( "span[name^='precondition_id_']", this).text($currentPosition);
			});
		}
	});
	
	
	$('#close-precondition-modal-btn').click(function(e) {
		$('#myModal').modal('hide')
	});
});


function searchSuccess(data, textStatus, jqXHR)
{
$('#precondition-result tbody').append(data);
}   
