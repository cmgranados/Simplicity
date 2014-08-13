$(document).ready(function(){

	$("#addRowInput").click(function(){
	  $('#tableInput > tbody:last').append("<tr id='row1'><td><input type='checkbox' value=''></td><td><input type='text' class='form-control'></td><td><input type='text' class='form-control'></td></tr>");
	});

	$("#deleteRowInput").click(function(){
		
	  $('#row1').remove();
	});



	$("#addRowOutput").click(function(){
	  //alert("The paragraph was clicked.");
	  $('#tableOutput > tbody:last').append("<tr><td><input type='checkbox' value=''></td><td><input type='text' class='form-control'></td><td><input type='text' class='form-control'></td></tr>");
	});

});