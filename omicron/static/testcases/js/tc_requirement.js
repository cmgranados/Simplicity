$( document ).ready(function() {
	
	$('#reqModal  #close-requirement-modal-btn').click(function(e) {
		$('#reqModal').modal('hide')
	});
	
	$( "#reqModal #search-requirements-btn" ).click(function() {
			$.ajax({
		        type: "POST",
		        url: "/kappa/requirements_ajax_search/",
		        data: { 
		            'q' : $('#q').val(),
		            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		        },
		        success: searchSuccess,
		        dataType: 'html'
		    });
	});
	
	function searchSuccess(data, textStatus, jqXHR) {
		$('#requirementResultTable tbody').html(data);
	} 
	
	$( "#add-requirement-row-btn" ).click(function() {
			$('#requirementResultTable input:checkbox:checked').parents("tr").each(function (index) {
					var $lastChar =1;
					$firstRow = "<tr> \
			            <td><input type='checkbox' name='requirementeCheckbox' value=''></td> \
			            <td><span name='requirementName' maxlength='11' readonly='readonly'>"+$(this).find('input:hidden[id=requirementTitleRetrieved]').val()+"</span></td> \
			            <input type='hidden' name='requirementId' value='"+$(this).find('input:hidden[id=requirementIdRetrieved]').val()+"'></input> \
			        </tr>"
			            $('#requirementsTable tbody').append($firstRow)
			});
			 $('#reqModal').modal('hide');
	});
	
	$( "#delete-requirement-rule-row-add" ).click(function() {
		$('#requirementsTable input:checkbox:checked').parents("tr").remove();
	});
});