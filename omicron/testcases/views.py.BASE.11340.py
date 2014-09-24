from django.shortcuts import render


def new_test_case(request):    
    return render(request, 'test_case_form_base.html')

