from datetime import datetime

from django.shortcuts import render_to_response, render
from rest_framework import viewsets

from kappa.businessrules.models import BusinessRule
from kappa.businessrules.serializers import BusinessRuleSerializer
from kappa.businessrules.utils import get_businessrules_types
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type
from simplicity_main.settings import STATE_REGISTERED


# Create your views here.
def new_businessrule_ajax(request):
    if request.method == "POST":
        business_rule = BusinessRule()
        newBusinessRuleTitle = request.POST.get('newBusinessRuleTitle', None)
        newBusinessRuleCode = request.POST.get('newBusinessRuleCode', None)
        businessRulesType = request.POST.get('businessRulesType', None)
        newBusinessRuleDescription = request.POST.get('newBusinessRuleDescription', None)
        business_rule.name = newBusinessRuleTitle
        business_rule.code = newBusinessRuleCode
        br_type = Type.objects.get(type_id = businessRulesType)
        business_rule.type = br_type
        business_rule.description = newBusinessRuleDescription
        business_rule.date_created = datetime.now()
        business_rule.date_modified = datetime.now()
        business_rule.state = State.objects.get(state_id=STATE_REGISTERED) 
        business_rule.save()
    return render_to_response('done.html')


def get_businessrules_types_ajax(request):
    br_type_list = get_businessrules_types();
    return render(request, 'ajax_businessrule_types_options.html', {'br_type_list' : br_type_list} )


class BusinessRuleView(viewsets.ModelViewSet):
    serializer_class = BusinessRuleSerializer
    queryset = BusinessRule.objects.all()
    #@api_view(('GET',))
    #@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    #def get(self, request):
    #    queryset = BusinessRule.objects.all()
    #    if request.accepted_renderer.format == 'html':
    #        data = {'businessrules': self.queryset}
    #        return Response(data, template_name='businessrule_list.html')
    #    serializer = BusinessRuleSerializer(instance=queryset)
    #    data = serializer.data
