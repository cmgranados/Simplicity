$(document).ready(function(){

	var $lastChar =1, $newRow;
	var $lastCharOutput =1, $newRowOutput;

	$("#add-row-input-btn").click(function(){
	 	if($('#input_table_body tr').length==0){
			$firstRow = "<tr> \
				<td><input type='checkbox' name='infFlowInput_checkbox_1' value=''></td>\
	            <td><input type='text' name='infFlowInput_1' maxlength='50' required /></td> \
	            <td><input type='text' name='infFlowInput_description_1' maxlength='50' required /></td> \
	            <td><input type='text' name='infFlowInput_datatype_1' maxlength='50' required /></td> \
	        </tr>"
			$('#inputTable > tbody:last').append($firstRow)			
	    } else {
	    	$get_lastID_inputTable();
			$('#inputTable > tbody:last').append($newRow);
	    };
		  
	});

	$("#add-row-output-btn").click(function(){
	  	if($('#output_table_body tr').length==0){
			$firstRow = "<tr> \
				<td><input type='checkbox' name='infFlowOutput_checkbox_1' value=''></td>\
	            <td><input type='text' name='infFlowOutput_1' maxlength='50' required /></td> \
	            <td><input type='text' name='infFlowOutput_description_1' maxlength='50' required /></td> \
	            <td><input type='text' name='infFlowOutput_datatype_1' maxlength='50' required /></td> \
	        </tr>"
			$('#outputTable > tbody:last').append($firstRow)			
	    } else {
	    	$get_lastID_outputTable();
			$('#outputTable > tbody:last').append($newRowOutput);
	    };
	});
	
	$get_lastID_inputTable = function(){
		var id = $('#inputTable tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	    	<td><input type='checkbox' name='infFlowInput_checkbox_"+$lastChar+"' value=''></td> \
            <td><input type='text' name='infFlowInput_"+$lastChar+"' maxlength='50' /></td> \
            <td><input type='text' name='infFlowInput_description_"+$lastChar+"' maxlength='50' /></td> \
            <td><input type='text' name='infFlowInput_datatype_"+$lastChar+"' maxlength='50' /></td> \
        </tr>"
    	return $newRow;
	}

	$get_lastID_outputTable = function(){
	    var id = $('#outputTable tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastCharOutput = $lastCharOutput + 1;
	    $newRowOutput = "<tr> \
	    	<td><input type='checkbox' name='infFlowOutput_checkbox_"+$lastCharOutput+"' value=''></td> \
            <td><input type='text' name='infFlowOutput_"+$lastCharOutput+"' maxlength='50' /></td> \
            <td><input type='text' name='infFlowOutput_description_"+$lastCharOutput+"' maxlength='50' /></td> \
            <td><input type='text' name='infFlowOutput_datatype_"+$lastCharOutput+"' maxlength='50' /></td> \
        </tr>"
    	return $newRowOutput;
	}

	$("#delete-row-input-btn").click(function(){
		$('#inputTable input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

	$("#delete-row-output-btn").click(function(){
		$('#outputTable input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});