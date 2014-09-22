from django.shortcuts import render

def new_test_case(request):    
    test_case_type_list = get_test_case_types();
    return render(request, 'test_case_form_base.html')

