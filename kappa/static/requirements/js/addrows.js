$(document).ready(function(){

	$("#addRowInput").click(function(){
	  //alert("The paragraph was clicked.");
	  $('#tableInput > tbody:last').append("<tr><td><input type='checkbox' value=''></td><td><input type='text' class='form-control'></td><td><input type='text' class='form-control'></td></tr>");
	});

	$("#addRowOutput").click(function(){
	  //alert("The paragraph was clicked.");
	  $('#tableOutput > tbody:last').append("<tr><td><input type='checkbox' value=''></td><td><input type='text' class='form-control'></td><td><input type='text' class='form-control'></td></tr>");
	});

});