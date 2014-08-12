# -*- coding: utf-8 -*-
from django import forms
from haystack.forms import SearchForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RequirementSearchForm(SearchForm):
	NEWER = 'desc'
	OLDER = 'asc'
	SORT_OPTIONS = (
				(NEWER , 'Más nuevo'),
				(OLDER , 'Más viejo')
	)
	q = forms.CharField(label="", max_length=255, required=False,)
	sort = forms.ChoiceField(label='Ordenar por',required=False, choices = SORT_OPTIONS)
	
	def search(self):
		sqs = super(RequirementSearchForm, self).search()
		sqs = sqs.order_by('pub_created')
		return sqs
	
	# Uni-form
	helper = FormHelper()
	helper.form_class = 'form-inline'
	helper.labels_uppercase = True
	helper.layout = Layout(
		Field('q', css_class='input-xlarge'),
		Field('sort', css_class='pull-right'),
		FormActions(
				Submit('save_changes', 'Save changes', css_class="btn-primary"),
				Submit('cancel', 'Cancel'),
		)
		
	)

class RequirementCreationForm(forms.Form):
    
    code = forms.CharField()
    date_created = forms.DateField()
    type = forms.ChoiceField()
    description = forms.Textarea()
    
    
