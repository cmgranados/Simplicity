import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from haystack.views import SearchView

from kappa.requirements.forms import RequirementForm1, RequirementForm2
from kappa.requirements.models import Requirement


# Create your views here.
class RequirementListView(ListView):
    model = Requirement

    def get_context_data(self, **kwargs):
        context = super(RequirementListView, self).get_context_data(**kwargs)
        return context


class FacetedSearchView(SearchView):
    def extra_context(self):
        extra = super(FacetedSearchView, self).extra_context()

        if self.results == []:
            extra['facets'] = self.form.search().facet_counts()
        else:
            extra['facets'] = self.results.facet_counts()

        return extra

class RequirementWizard(SessionWizardView):
    template_name = "requirement_form.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        
        return render_to_response("done.html", {'form_data': form_data})
    
def process_form_data(form_list):
    form_data = [form.cleaned for form in form_list]
    
    logging.debug(form_data[0]['subject'])
    logging.debug(form_data[1]['sender'])
    logging.debug(form_data[2]['message'])
    
    return form_data
    
    