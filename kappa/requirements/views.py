import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from haystack.views import SearchView

from kappa.requirements.forms import RequirementForm1, RequirementForm2, RequirementForm3
from kappa.requirements.models import Requirement

FORMS = [("requirementform1", RequirementForm1),
         ("requirementform2", RequirementForm2),
         ("requirementform3", RequirementForm3)]


TEMPLATES = {"requirementform1": "requirementform1.html",
             "requirementform2": "requirementform2.html",
             "requirementform3": "requirementform3.html"}

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
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('done.html')
