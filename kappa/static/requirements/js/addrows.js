$(document).ready(function(){

	var $lastChar =1, $newRow;
	var $lastCharOutput =1, $newRowOutput;

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

	$get_lastID_outputTable = function(){
		var $id = $('#tableOutput tr:last-child td:first-child input').attr("name");
	    $lastCharOutput = parseInt($id.substr($id.length - 2), 10);
	    $lastCharOutput = $lastCharOutput + 1;
	    $newRowOutput = "<tr> \
	    	<td><input type='checkbox' name='flow_output_checkbox_0"+$lastCharOutput+"' value=''></td> \
            <td><input type='text' name='flow_output_0"+$lastCharOutput+"' maxlength='255' /></td> \
            <td><input type='text' name='flow_output_value_0"+$lastCharOutput+"' maxlength='255' /></td> \
        </tr>"
    	return $newRowOutput;
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

	$("#addRowOutput").click(function(){
	  	if($('#output_table_body tr').length==0){
			$firstRow = "<tr> \
				<td><input type='checkbox' name='flow_output_checkbox_01' value=''></td>\
	            <td><input type='text' name='flow_output_01' maxlength='255' required /></td> \
	            <td><input type='text' name='flow_output_value_01' maxlength='255' required /></td> \
	        </tr>"
			$('#tableOutput > tbody:last').append($firstRow)			
	    } else {
	    	$get_lastID_outputTable();
			$('#tableOutput > tbody:last').append($newRowOutput);
	    };
	});

	$("#deleteRowInput").click(function(){
		$('#tableInput input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

	$("#deleteRowOutput").click(function(){
		$('#tableOutput input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});