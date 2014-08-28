from datetime import datetime

from django.test import TestCase

from kappa.preconditions.models import PreconditionDescription, PreconditionRequirement, Precondition
from kappa.requirements.models import Requirement
from shared.states_simplicity.models import State, StateType
from shared.types_simplicity.models import Type, TypeClassification


# MODELS
class PreconditionTestCase(TestCase):
    
    def create_precondition(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        return Precondition.objects.create(requirement=requirement_instance)
        
    def test_precondition_creation(self):
        precondition_instance = self.create_precondition()
        self.assertTrue(isinstance(precondition_instance, Precondition))
        self.assertEqual(precondition_instance.__unicode__(), precondition_instance.precondition_id)
        self.assertEqual(precondition_instance._meta.db_table,  'kp_pco_precondition')
        
class PreconditionDescriptionTestCase(TestCase):
    
    def create_description(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        precondition_instance= Precondition.objects.create(requirement=requirement_instance)
        
        return PreconditionDescription.objects.create(description="Precondition description example", precondition= precondition_instance )
        
    def test_description_creation(self):
        description_instance = self.create_description()
        self.assertTrue(isinstance(description_instance, PreconditionDescription))
        self.assertEqual(description_instance.__unicode__(), description_instance.precondition)
        self.assertEqual(description_instance._meta.db_table,  'kp_pco_precondition_description')
    
    
class PreconditionRequirementTestCase(TestCase):
    
    def create_requirement(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        precondition_instance= Precondition.objects.create(requirement=requirement_instance)
        
        return PreconditionRequirement.objects.create(requirement=requirement_instance, precondition= precondition_instance)
    
    def test_requirement_creation(self):
        requirement_instance = self.create_requirement()
        self.assertTrue(isinstance(requirement_instance, PreconditionRequirement))
        self.assertEqual(requirement_instance.__unicode__(), requirement_instance.precondition)
        self.assertEqual(requirement_instance._meta.db_table,  'kp_pco_precondition_requirement')
    
    
       
    