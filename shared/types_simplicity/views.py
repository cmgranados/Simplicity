from django.shortcuts import render

from shared.types_simplicity.utils import get_datatypes_types

# Create your views here.
def get_data_types_ajax(request):
    datatype_type_list = get_datatypes_types();
    return render(request, 'ajax_datatypes_options.html', {'dt_type_list' : datatype_type_list} )