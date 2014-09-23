$(document).ready(function(){

	function getBrTypesSelectOptions(){
		$request = $.ajax({
			        type: "POST",
			        url: "/kappa/get_businessrules_types_ajax",
			        data: { 
			        	csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
			        },
			        success : searchSuccessBrTypes,
		            error : function(xhr,errmsg,err) {
		                showMessage('message','error', '<strong>Ocurrio un error</strong>: ' + errmsg);
		                $('#message').attr("class", getClassByType('error'));
		            },
			        dataType: 'html'
		});
	}
});
