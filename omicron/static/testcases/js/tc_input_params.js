$(document).ready(function(){

	var $lastChar =1, $newRow;
	
	$('#input-params-form').validate();

	$get_lastID_criteriaTable = function(){
		var id = $('#tableInputParams tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	    	<td><input type='checkbox' name='criteria_checkbox_"+$lastChar+"' value='' ></td> \
            <td><input type='text' name='criteria_name_"+$lastChar+"' maxlength='255' required/></td> \
            <td><input type='text' name='criteria_description_"+$lastChar+"' maxlength='255' required/></td> \
        </tr>"
    	return $newRow;
	}

	$("#addRowInput").click(function(){

	 	if ($('#input-params-form').valid()) {
			if ($('#table_input_params_body tr').length == 0) {
				$firstRow = "<tr> \
				<td><input type='checkbox' name='criteria_checkbox_1' value=''></td>\
	            <td><input type='text'  maxlength='255' required name='criteria_name_1' required/></td> \
	            <td><input type='text'  maxlength='255' required name='criteria_description_1' required/></td> \
	        </tr>"
				$('#tableInputParams > tbody:last').append($firstRow)
			} else {
				$get_lastID_criteriaTable();
				$('#tableInputParams > tbody:last').append($newRow);
			}
		}
		  
	});

	$("#deleteRowInput").click(function(){
		$('#tableInputParams input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});