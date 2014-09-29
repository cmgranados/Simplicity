$(document).ready(function(){

	var $lastChar =1, $newRow;
	
	$('#process-form').validate();

	$get_lastID_processTable = function(){
		var id = $('#tableProcess tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	    	<td><input type='checkbox' name='step_checkbox_"+$lastChar+"' value='' ></td> \
            <td><input type='text' name='step_number_"+$lastChar+"' maxlength='255' required/></td> \
            <td><input type='text' name='step_activity_"+$lastChar+"' maxlength='255' required/></td> \
        </tr>"
    	return $newRow;
	}

	$("#addRowStep").click(function(){
	 	if ($('#process-form').valid()) {
			if ($('#table_process_params_body tr').length == 0) {
				$firstRow = "<tr> \
				<td><input type='checkbox' name='step_checkbox_1' value=''></td>\
	            <td><input type='text'  maxlength='255' required name='step_number_1' required/></td> \
	            <td><input type='text'  maxlength='255' required name='step_activity_1' required/></td> \
	        </tr>"
				$('#tableProcess > tbody:last').append($firstRow)
			} else {
				$get_lastID_processTable();
				$('#tableProcess > tbody:last').append($newRow);
			}
		}
		  
	});

	$("#deleteRowStep").click(function(){
		$('#tableProcess input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});