$(document).ready(function(){
	
	$("#delete-requirement-btn").click(function(){
		if($('#requirementsTable input:checkbox:checked').length > 0){
			bootbox.confirm("¿Está seguro de que desea eliminar los requisitos seleccionados?", function(result){
				if(result){
					$('#requirementsTable input:checkbox:checked').each(function () {
						
				           
					});
				}
			});
		}else{
			alert("No hay ningún requisito seleccionado para eliminar.")
		}
	});
	
});