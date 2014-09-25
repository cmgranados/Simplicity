$(document).ready(function(){

	var $lastChar =1, $newRow;
	
	$('#input-params-form').validate();

	$get_lastID_input_paramsTable = function(){
		var id = $('#tableInputParams tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	    	<td><input type='checkbox' name='input_params_checkbox_"+$lastChar+"' value='' ></td> \
            <td><input type='text' name='input_params_name_"+$lastChar+"' maxlength='255' required/></td> \
            <td><input type='text' name='input_params_description_"+$lastChar+"' maxlength='255' required/></td> \
            <td><select class='form-control' id='input_params_datatype_"+$lastChar+"' name='input_params_datatype_"+$lastChar+"'></select></td> \
        </tr>"
    	return $newRow;
	}

	$("#addRowInput").click(function(){

	 	if ($('#input-params-form').valid()) {
			if ($('#table_input_params_body tr').length == 0) {
				$firstRow = "<tr> \
				<td><input type='checkbox' name='input_params_checkbox_1' value=''></td>\
	            <td><input type='text'  maxlength='255' required name='input_params_name_1' required/></td> \
	            <td><input type='text'  maxlength='255' required name='input_params_description_1' required/></td> \
				<td><select class='form-control' id='input_params_datatype_1' name='input_params_datatype_1'></select></td> \
	        </tr>"
				$('#tableInputParams > tbody:last').append($firstRow)
			} else {
				$get_lastID_input_paramsTable();
				$('#tableInputParams > tbody:last').append($newRow);
			}
			getDataTypesOptions("tableInputParams");
		}
		  
	});

	$("#deleteRowInput").click(function(){
		$('#tableInputParams input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});