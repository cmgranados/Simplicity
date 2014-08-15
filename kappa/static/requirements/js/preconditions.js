$( document ).ready(function() {
	var $lastChar =1, $newRow;
	var $descriptionType = 'Descripción';
	
	$( "#add_DescriptionRow" ).click(function() {
		if($('#precondition_table tbody tr').length == 0){
			var $lastChar =1;
			var $description = $('#description_textarea').val();
			$firstRow = "<tr> \
	            <td><input type='checkbox' name='precondition_checkbox_01' value=''></td> \
	            <td><span name='precondition_id_01' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
	            <td><span name='precondition_description_01' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
	            <td><span name='precondition_type_01' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
	        </tr>"
			$('#precondition_table tbody').append($firstRow)
			$firstRowHidden = "<input type='hidden' id='precondition_id_01_hidden' value='"+$lastChar+"'></input> {{ previous_fields|safe }}"
			$('body').append($firstRowHidden)
	    } else {
	    	$get_lastID();
			$('#precondition_table > tbody:last').append($newRow);
	    };
	    $('#myModal').modal('hide');
		  
	});
	
	$get_lastID = function(){
	    var $id = $('#precondition_table tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt($id.substr($id.length - 2), 10);
	    var  $description = $('#description_textarea').val();
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
            <td><input type='checkbox' name='precondition_checkbox_0"+$lastChar+"' value=''></td> \
            <td><span name='precondition_id_0"+$lastChar+"' maxlength='11' readonly='readonly'>"+$lastChar+"</span></td> \
            <td><span name='precondition_description_0"+$lastChar+"' maxlength='11' readonly='readonly'>"+$description+"</span></td> \
            <td><span name='precondition_type_0"+$lastChar+"' maxlength='11' readonly='readonly'>"+$descriptionType+"</span></td> \
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
});

