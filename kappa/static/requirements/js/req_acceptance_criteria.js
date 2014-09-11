$(document).ready(function(){

	var $lastChar =1, $newRow;
	
	$('#criteria-form').validate();

	$get_lastID_criteriaTable = function(){
		var id = $('#tableCriteria tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	    	<td><input type='checkbox' name='criteria_checkbox_"+$lastChar+"' value=''></td> \
            <td><input type='text' name='criteria_name_"+$lastChar+"' maxlength='255' /></td> \
            <td><input type='text' name='criteria_description_"+$lastChar+"' maxlength='255' /></td> \
        </tr>"
    	return $newRow;
	}

	$("#addRowCriteria").click(function(){
		
	 	if ($('#criteria-form').valid()) {
			if ($('#table_criteria_body tr').length == 0) {
				$firstRow = "<tr> \
				<td><input type='checkbox' name='criteria_checkbox_1' value=''></td>\
	            <td><input type='text' name='criteria_name_1' maxlength='255' required /></td> \
	            <td><input type='text' name='criteria_description_1' maxlength='255' required /></td> \
	        </tr>"
				$('#tableCriteria > tbody:last').append($firstRow)
			} else {
				$get_lastID_criteriaTable();
				$('#tableCriteria > tbody:last').append($newRow);
			}
		}
		  
	});

	$("#deleteRowCriteria").click(function(){
		$('#tableCriteria input:checkbox:checked').parents("tr").remove();
		$lastChar = $lastChar-2;
		
	});

});