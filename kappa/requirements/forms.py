# -*- coding: utf-8 -*-
from django import forms
from haystack.forms import SearchForm
from haystack.inputs import AutoQuery


class RequirementSearchForm(SearchForm):
    q = forms.CharField(label="", max_length=255, required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control",'required': 'true',
                            'placeholder': 'Buscar ...'}))
    #my_fieldname = forms.CharField(label="MySearchLabel", max_length=255, required=False)

    def search(self):
        sqs = super(RequirementSearchForm, self).search()

        #if self.is_valid() and self.cleaned_data['my_fieldname']:
            #sqs = sqs.filter(my_fieldname=AutoQuery(self.cleaned_data['my_fieldname']))

        return sqs
