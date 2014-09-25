function getDataTypesOptions(tableName){
		$.ajax({
	        type: "POST",
	        url: "/types/get_data_types_ajax/",
	        data: { 
	            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
	        },
	        success: function(data, textStatus, jqXHR) {
	    		$('#'+tableName+' tr:last-child td:last-child select').append(data);
	    	},
	        dataType: 'html'
	    });
	}