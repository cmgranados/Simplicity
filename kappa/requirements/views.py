from django.views.generic.list import ListView
from kappa.requirements.models import Requirement

# Create your views here.
class RequirementListView(ListView):
    
    model = Requirement

    def get_context_data(self, **kwargs):
        context = super(RequirementListView, self).get_context_data(**kwargs)
        return context