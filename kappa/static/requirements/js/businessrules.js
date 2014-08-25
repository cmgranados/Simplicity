$( document ).ready(function() {
	var $lastChar =1, $newRow;
	var $descriptionType = 'Descripci�n';
	var $requirementType = 'Requisito';
	
	$( "#searchBusinessRules" ).click(function() {
		$.ajax({
	        type: "POST",
	        url: "/search-businessrules/",
	        data: { 
	            'br' : $('#br').val(),
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: searchSuccessBr,
	        dataType: 'html'
	    });
	});
});

function searchSuccessBr(data, textStatus, jqXHR)
{
$('#businessrule-result tbody').append(data);
} 
