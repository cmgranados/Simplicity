$(document).ready(function(){
	
	$("#delete-requirement-btn").click(function(){
		if($('#requirementsTable input:checkbox:checked').length > 0){
			bootbox.confirm("¿Está seguro de que desea eliminar los requisitos seleccionados?", function(result){
				if(result){
					$('#requirementsTable input:checkbox:checked').each(function () {
						
						var id = $( this ).parents("tr").find("#requirement_id").val();
						
						$.ajax({
							type: "POST",
							url: '/kappa/requirements/delete_requirement_ajax',
							data: { 
					            'id': id,
					            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
					        },
							success: function(data) {
					            // update results
					        },
					        error: function(xhr, textStatus, errorThrown) {
					            alert("Error al eliminar requisitos.");
					        }
							});
					});
				}
			});
		}else{
			alert("No hay ningún requisito seleccionado para eliminar.")
		}
	});
	
});