# -*- coding: utf-8 -*-
from django import forms
from haystack.forms import SearchForm


class RequirementSearchForm(SearchForm):
	NEWER = 'desc'
	OLDER = 'asc'
	SORT_OPTIONS = (
				(NEWER , 'Más nuevo'),
				(OLDER , 'Más viejo')
	)
	q = forms.CharField(label="", max_length=255, required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control form-control-large search-input",'required': 'true',
                            'placeholder': 'Buscar ...'}))
	sort = forms.ChoiceField(label="Ordernar por", required=False, choices=SORT_OPTIONS)
	
	def search(self):
		sqs = super(RequirementSearchForm, self).search()
		sqs = sqs.order_by('pub_created')
		return sqs

# Requirements Wizard
class RequirementForm1(forms.Form):
	title = forms.CharField()
	code = forms.CharField()
	date_created = forms.CharField()

class RequirementForm2(forms.Form):
	# precondition table
	requirementform2 = forms.CharField()
	
class RequirementForm3(forms.Form):
	# business rules table
	requirementform3 = forms.CharField()

class RequirementForm4(forms.Form):
	# information flows - inputs table, outputs table
	requirementform4 = forms.CharField()

class RequirementForm5(forms.Form):
	# acceptance criteria
	requirementform5 = forms.CharField()
