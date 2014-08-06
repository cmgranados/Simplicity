# -*- coding: utf-8 -*-
from django import forms
from haystack.forms import SearchForm
from haystack.inputs import AutoQuery
import datetime


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

class RequirementCreationForm(forms.Form):
    
    code = forms.CharField()
    date_created = forms.DateField()
    type = forms.ChoiceField()
    description = forms.Textarea()
    
