# -*- coding: utf-8 -*-
import datetime

from django import forms
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from haystack.forms import SearchForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from shared.types_simplicity.models import Type, TypeClassification
from simplicity_main.constants import MyConstants


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

# Requirements Wizard
class RequirementForm1(forms.Form):
	title = forms.CharField()
	code = forms.CharField()
	date_created = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, 
								widget=SelectDateWidget(years=range(datetime.date.today().year, 1989, -1)))
	
	type = forms.ModelChoiceField(queryset=Type.objects.filter(type_classification_id=TypeClassification.objects.filter(code='REQ')), 
								widget=forms.Select(attrs={'class':'selector'}))
	
	description = forms.CharField(widget=forms.Textarea)
	
	def __init__(self, *args, **kwargs):
		super(RequirementForm1, self).__init__(*args, **kwargs)
		self.fields['title'].label = "Nombre"
		self.fields['code'].label = "Código"
		self.fields['date_created'].label = "Fecha de creación"
 		self.fields['type'].label = "Tipo de Requisito"
		self.fields['description'].label = "Definición de Requisito"

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
