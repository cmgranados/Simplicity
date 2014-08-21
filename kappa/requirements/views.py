import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from kappa.requirements.forms import RequirementForm1, RequirementForm2, RequirementForm3, RequirementForm4, RequirementForm5
from kappa.requirements.models import Requirement


FORMS = [
#     ("requirement_form_1", RequirementForm1),
    ("requirement_form_2", RequirementForm2),
    ("requirement_form_3", RequirementForm3),
    ("requirement_form_4", RequirementForm4),
    ("requirement_form_5", RequirementForm5)]


TEMPLATES = {
    "requirement_form_1": "requirement_form_1.html",
    "requirement_form_2": "requirement_form_2.html",
    "requirement_form_3": "requirement_form_3.html",
    "requirement_form_4": "requirement_form_4.html",
    "requirement_form_5": "requirement_form_5.html"}

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


def searchRequirements(request):
    if not request.POST.get('q', '') :
        content_auto_v = "descripcion"
    else:
        content_auto_v=request.POST.get('q', '')
        
    requirements = SearchQuerySet().filter(text=content_auto_v)
    return render_to_response('ajax_search.html', {'requirements': requirements})
