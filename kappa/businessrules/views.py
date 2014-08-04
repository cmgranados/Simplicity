from rest_framework import viewsets

from kappa.businessrules.models import BusinessRule
from kappa.businessrules.serializers import BusinessRuleSerializer


# Create your views here.
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
    #    return Response(data)
