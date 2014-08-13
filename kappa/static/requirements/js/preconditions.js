$( document ).ready(function() {
	var $lastChar =1, $newRow;
	
	$( "#add_DescriptionRow" ).click(function() {
		if($('#precondition_description tr').length==0){
			$firstRow = "<tr> \
	            <td><input type='text' name='reg_no_01' maxlength='255' required /></td> \
	            <td><input type='text' name='subjects_01' maxlength='255' required /></td> \
	            <td><input type='number' name='max_marks_01' maxlength='11' required /></td> \
	            <td><input type='number' name='max_obtained_01' maxlength='11' required /></td> \
	        </tr>"
			$('#precondition_table tbody > tbody > tr').append($firstRow)			
	    } else {
	    	$get_lastID();
			$('#precondition_table tbody > tbody > tr').append($newRow);
	    };
		  
	});
	
	$get_lastID = function(){
	    var $id = $('#precondition_table tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt($id.substr($id.length - 2), 10);
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
            <td><input type='text' name='reg_no_0"+$lastChar+"' maxlength='255' /></td> \
            <td><input type='text' name='subjects_0"+$lastChar+"' maxlength='255' /></td> \
            <td><input type='number' name='max_marks_0"+$lastChar+"' maxlength='11' /></td> \
            <td><input type='number' name='max_obtained_0"+$lastChar+"' maxlength='11' /></td> \
        </tr>"
     return $newRow;
	}
});

