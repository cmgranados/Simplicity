from django.views.generic.list import ListView
from kappa.requirements.models import Requirement
from haystack.views import SearchView


from .forms import RequirementCreationForm
from django.shortcuts import render


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

def new_requirement(request):
    form = RequirementCreationForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    return render(request, 'signup.html', {'form': form})

