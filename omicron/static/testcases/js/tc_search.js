$(document).ready(function() {
	
	$( "#searchTestCasesForm" ).submit(function(event) {
		
		event.preventDefault();
		
		$request = $.ajax({
	        type: "POST",
	        url: "/omicron/testcases/search",
	        data: { 
	        	q: $('#q').val(),
	        	csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success : searchSuccess,
            error : function(xhr,errmsg,err) {
                showMessage('message','error', '<strong>Ocurrio un error</strong>: ' + errmsg);
                $('#message').attr("class", getClassByType('error'));
            },
	        dataType: 'html'
	    });
	});
	
	function showMessage(divId, type, message) {
		divClass = getClassByType(type);
		divHtml = '';
		closeBtn = ' <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>';
		
		//append message div
		mainDivHtml = '<div id="' + divId +'" class="alert alert-info alert-dismissible" role="alert"></div>';
		$('#messages').html(mainDivHtml);
		$('#messages').attr("class", 'div-visible');
		
		
		//append content to message div
		divHtml += closeBtn + message;
		$('#' + divId).html(divHtml);
		//define class value to message div
		$(divId).attr("class", divClass);
	}

	function getClassByType(type) {
		divClass = '';
		if(type == 'error') {
			divClass = 'alert alert-danger alert-dismissible div-visible';
		} else if(type == 'success') {
			divClass = 'alert alert-success alert-dismissible div-visible';
		} else if(type == 'info') {
			divClass = 'alert alert-info alert-dismissible div-visible';
		}
		
		return divClass;
	}

	function searchSuccess(data, textStatus, jqXHR) {
		$('#test-cases-tbl tbody').html(data);
	}  
	
});

 

