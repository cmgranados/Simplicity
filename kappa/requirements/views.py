import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.list import ListView
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from kappa.requirements.forms import RequirementForm1, RequirementForm2, RequirementForm3, RequirementForm4, RequirementForm5
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


def searchRequirements(request):
    if not request.POST.get('q', '') :
        content_auto_v = "descripcion"
    else:
        content_auto_v=request.POST.get('q', '')
        
    requirements = SearchQuerySet().filter(text=content_auto_v)
    return render_to_response('ajax_search.html', {'requirements': requirements})


def new_requirement(request):
    return render(request, 'requirement_form_base.html')
