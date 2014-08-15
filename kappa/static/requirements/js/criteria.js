$(document).ready(function(){

	var $lastChar =1, $newRow;

	$get_lastID_inputTable = function(){
		var $id = $('#tableInput tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt($id.substr($id.length - 2), 10);
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	    	<td><input type='checkbox' name='flow_input_checkbox_0"+$lastChar+"' value=''></td> \
            <td><input type='text' name='flow_input_0"+$lastChar+"' maxlength='255' /></td> \
            <td><input type='text' name='flow_input_value_0"+$lastChar+"' maxlength='255' /></td> \
        </tr>"
    	return $newRow;
	}

	$("#addRowInput").click(function(){
	 	if($('#input_table_body tr').length==0){
			$firstRow = "<tr> \
				<td><input type='checkbox' name='flow_input_checkbox_01' value=''></td>\
	            <td><input type='text' name='flow_input_01' maxlength='255' required /></td> \
	            <td><input type='text' name='flow_input_value_01' maxlength='255' required /></td> \
	        </tr>"
			$('#tableInput > tbody:last').append($firstRow)			
	    } else {
	    	$get_lastID_inputTable();
			$('#tableInput > tbody:last').append($newRow);
	    };
		  
	});

	$("#deleteRowInput").click(function(){
		$('#tableInput input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});