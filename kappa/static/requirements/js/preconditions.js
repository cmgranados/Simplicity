$( document ).ready(function() {
	$( "#precondition_description" ).click(function() {
		  alert( "Handler for .click() called." );
		  $('#preconditions_table').append('<tr><td>my data</td><td>more data</td></tr>');
		});
});
