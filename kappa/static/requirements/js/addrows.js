$(document).ready(function(){

	var idInput = 0;

	$("#addRowInput").click(function(){
	  $('#tableInput > tbody:last').append("<tr id='row"+idInput+"'><td><input type='checkbox' value=''></td><td><input type='text' class='form-control'></td><td><input type='text' class='form-control'></td></tr>");

	  idInput+=1;

	});

	$("#deleteRowInput").click(function(){
		
	
	});

	$("#addRowOutput").click(function(){
	  //alert("The paragraph was clicked.");
	  $('#tableOutput > tbody:last').append("<tr><td><input type='checkbox' value=''></td><td><input type='text' class='form-control'></td><td><input type='text' class='form-control'></td></tr>");
	});

});