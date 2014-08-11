# -*- coding: utf-8 -*-
import datetime

from django import forms
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from haystack.forms import SearchForm

from shared.types_simplicity.models import Type, TypeClassification
from simplicity_main.constants import MyConstants


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
	date_created = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, 
								widget=SelectDateWidget(years=range(datetime.date.today().year, 1989, -1)))
	
 	#==========================================================================
 	# type = forms.ModelChoiceField(queryset=Type.objects.get(type_classification=TypeClassification.objects.get(code=MyConstants.TYPE_CLASSIFICATION_CODE.get("REQUIREMENT"))),
  #                                       widget=forms.Select(attrs={'class':'selector'}))
  #==========================================================================

	#===========================================================================
	# type = forms.ModelChoiceField(queryset=Type.objects.all(), 
	# 							widget=forms.Select(attrs={'class':'selector'}))
	#===========================================================================
	
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
