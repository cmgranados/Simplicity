# -*- coding: utf-8 -*-
import datetime
import logging

from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.layout import Layout, Field, Submit, Fieldset, ButtonHolder
from django import forms
from django.conf import settings
from django.contrib.admin import helpers
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget
from haystack.backends import SQ
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

from kappa.businessrules.models import BusinessRule
from kappa.requirements.models import Requirement
from shared.types_simplicity.models import Type, TypeClassification
from simplicity_main.constants import MyConstants


# Get an instance of a logger
logger = logging.getLogger('simplicity_main.kappa.requirements.forms')

class RequirementSearchForm(SearchForm):
	NEWER = 'desc'
	OLDER = 'asc'
	SORT_OPTIONS = (
				(NEWER , 'Más nuevo'),
				(OLDER , 'Más viejo')
	)
	q = forms.CharField(label="", max_length=255, required=False,)
	start_date = forms.DateField(label='Fecha inicio', required=False)
	end_date = forms.DateField(label='Fecha fin', required=False)
	
	type = forms.ModelChoiceField(label="Tipo", required=False, queryset=Type.objects.filter(type_id__in=Requirement.objects.values_list('type_id').distinct()), 
								widget=forms.Select(attrs={'class':'selector'}), empty_label="Seleccione una opción ...")
	sort = forms.ChoiceField(label='Ordenar por', required=False, choices = SORT_OPTIONS)
	
	@property
	def helper(self):
	    logger.debug('Something went wrong!')
	    helper = FormHelper(self)
	    helper.form_action = reverse('search')
	    helper.form_method = 'GET'
	    return helper


	def search(self):
		sqs = super(RequirementSearchForm, self).search()
		sqs = sqs.models(Requirement)
		
		sort_value = "pub_created"
		
		if not self.is_valid():
			return self.no_query_found()
		
		if not self.cleaned_data['q']:
			logger.debug('empty q value')
			return self.no_query_found()
		
		 # Check to see if a start_date was chosen.
		if self.cleaned_data['type']:
			sqs = sqs.filter(type_id__gte=self.cleaned_data.get('type').type_id)
			
		 # Check to see if a start_date was chosen.
		if self.cleaned_data['start_date']:
			sqs = sqs.filter(pub_created__gte=self.cleaned_data['start_date'])
		
		# Check to see if an end_date was chosen.
		if self.cleaned_data['end_date']:
			sqs = sqs.filter(pub_created__lte=self.cleaned_data['end_date'])
		
		if self.cleaned_data['sort']:
			if str(self.cleaned_data.get('sort')) == 'desc':
				sort_value = "-pub_created"
		
		sqs = sqs.order_by(sort_value)
			
		return sqs
	
	def no_query_found(self):
		logger.debug('load all!')
		return self.searchqueryset.all()
	
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
	hidden = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
	
class RequirementForm3(forms.Form):
	# business rules table
	requirementform3 = forms.CharField()

class RequirementForm4(forms.Form):
	# information flows - inputs table, outputs table
	requirementform4 = forms.CharField()

class RequirementForm5(forms.Form):
	# acceptance criteria
	requirementform5 = forms.CharField()
