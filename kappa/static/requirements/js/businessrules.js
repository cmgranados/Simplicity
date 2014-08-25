$( document ).ready(function() {
	var $lastChar =1, $newRow;
	
	$( "#searchBusinessRules" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/kappa/businessrules/",
	        data: { 
	            'br' : $('#br').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: searchSuccessBr,
	        dataType: 'html'
	    });
	});
	
	$get_lastID_br = function(obj){
	    var id = $('#businessrules_table tr:last-child td:first-child input').attr("name");
	    $lastChar = parseInt(id.substr(id.lastIndexOf("_") + 1, id.length));
	    $lastChar = $lastChar + 1;
	    $newRow = "<tr> \
	        <td><input type='checkbox' name='businessrule_checkbox_"+$lastChar+"' value=''></td> \
	        <td><span name='businessrule_name_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$(obj).find('input:hidden[name=businessrule_name]').val()+"</span></td> \
	        <td><span name='businessrule_description_"+$lastChar+"' maxlength='11' readonly='readonly'>"+$(obj).find('input:hidden[name=businessrule_description]').val()+"</span></td> \
	    </tr>"
	 return $newRow;
	}


	function searchSuccessBr(data, textStatus, jqXHR)
	{
	$('#businessrule-result tbody').append(data);
	} 
	
	$( "#addBusinessRuleRow" ).click(function() {
		$('#businessrule-result input:checkbox:checked').parents("tr").each(function (index) {
			if($('#businessrules_table tbody tr') != null && $('#businessrules_table tbody tr').length == 0){
				var $lastChar =1;
				$firstRow = "<tr> \
		            <td><input type='checkbox' name='businessrule_checkbox_1' value=''></td> \
		            <td><span name='businessrule_name_1' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[name=businessrule_name]').val()+"</span></td> \
		            <td><span name='businessrule_description_1' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[name=businessrule_description]').val()+"</span></td> \
		        </tr>"
		            $('#businessrules_table tbody').append($firstRow)
					$firstRowHiddenId = "<input type='hidden' id='businessrule_id_1_hidden' name='businessrule_id_1_hidden' value='"+$(this).find('input:hidden[name=businessrule_id]').val()+"'></input>"
					$('#form_requirements').append($firstRowHiddenId)
			} else {
				$get_lastID_br($(this));
				$('#businessrules_table > tbody:last').append($newRow);
			}
		});
	});
	
	$( "#deleteBusinessRuleRow" ).click(function() {
		$('#businessrules_table input:checkbox:checked').parents("tr").remove();
		if($('#businessrules_table tbody tr').length > 0){
			$('#businessrules_table > tbody  > tr').each(function(index) {
				var $currentPosition = index+1;
				$("input[type='checkbox'][name^='businessrule_checkbox_']").attr( "name", "businessrule_checkbox_"+$currentPosition);
				$( "span[name^='businessrule_name_']", this).attr( "name", "businessrule_name_"+$currentPosition);
				$( "span[name^='businessrule_description_']", this).attr( "name", "businessrule_description_"+$currentPosition);
			});
		}
	});
	
});
