from datetime import datetime

from django.test import TestCase

from kappa.businessrules.models import BusinessRule
from kappa.requirements.models import Requirement, RequirementBusinessRule, \
    RequirementInput, RequirementOutput, AcceptanceCriteria, RequirementAuthor
from shared.states_simplicity.models import State, StateType
from shared.types_simplicity.models import Type, TypeClassification
from django.contrib.auth.models import User


# MODELS
class RequirementTestCase(TestCase):
    
    def create_requirement(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved)
        requirement_retrieved = Requirement.objects.create(title ="tit", description="desc", 
                                                           type = type_retrieved, state = state_retrieved, 
                                                           date_created = datetime.now(), date_modified= datetime.now(), 
                                                           code = "1", keywords= "keyword", is_active="1")
        return requirement_retrieved
        
    def test_requirement_creation(self):
        requirement_instance = self.create_requirement()
        self.assertTrue(isinstance(requirement_instance, Requirement))
        self.assertEqual(requirement_instance.__unicode__(), requirement_instance.title)
        self.assertEqual(requirement_instance._meta.db_table,  'kp_req_requirement')
        
class RequirementBusinessRuleTestCase(TestCase):
    
    def create_requirement_businessrule(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1") 
        
        businessrule= BusinessRule.objects.create(name="Req_test", description="description example", type=type_retrieved, state_type=state_retrieved,
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123")
        
        return RequirementBusinessRule.objects.create(requirement= requirement_instance, business_rule=businessrule)
        
    def test_requirement_businessrule_creation(self):
        requirement_businessrule_instance = self.create_requirement_businessrule()
        self.assertTrue(isinstance(requirement_businessrule_instance, RequirementBusinessRule))
        self.assertEqual(requirement_businessrule_instance.__unicode__(), requirement_businessrule_instance.requirement_business_rule_id)
        self.assertEqual(requirement_businessrule_instance._meta.db_table,  'kp_req_requirement_business_rule')
    

class RequirementInputTestCase(TestCase):
    
    def create_requirement_input(self):
        
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        
        return RequirementInput.objects.create(requirement= requirement_instance, input="input_test", value="input_value_test")
        
    def test_requirement_businessrule_creation(self):
        requirement_input_instance = self.create_requirement_input()
        self.assertTrue(isinstance(requirement_input_instance, RequirementInput))
        self.assertEqual(requirement_input_instance.__unicode__(), requirement_input_instance.requirement_input_id)
        self.assertEqual(requirement_input_instance._meta.db_table,  'kp_req_requirement_input')
    
    
class RequirementOutputTestCase(TestCase):
    
    def create_requirement_output(self):
        
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        
        return RequirementOutput.objects.create(requirement= requirement_instance, output="output_test", value="output_value_test")
        
    def test_requirement_businessrule_creation(self):
        requirement_output_instance = self.create_requirement_output()
        self.assertTrue(isinstance(requirement_output_instance, RequirementOutput))
        self.assertEqual(requirement_output_instance.__unicode__(), requirement_output_instance.requirement_output_id)
        self.assertEqual(requirement_output_instance._meta.db_table,  'kp_req_requirement_output')  
        

class RequirementAcceptanceCriteriaTestCase(TestCase):
    
    def create_requirement_acceptance_criteria(self):
        
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        
        return AcceptanceCriteria.objects.create(name= "acc_criteria_name", description="acc_criteria_description",
                                                  requirement= requirement_instance, date_created=datetime.now(), date_modified=datetime.now(), code="")
    
    def test_requirement_businessrule_creation(self):
        requirement_acceptance_criteria_instance = self.create_requirement_acceptance_criteria()
        self.assertTrue(isinstance(requirement_acceptance_criteria_instance, AcceptanceCriteria))
        self.assertEqual(requirement_acceptance_criteria_instance.__unicode__(), requirement_acceptance_criteria_instance.name)
        self.assertEqual(requirement_acceptance_criteria_instance._meta.db_table,  'kp_req_acceptance_criteria') 
      
        
class RequirementAuthorTestCase(TestCase):
    
    def create_requirement_author(self):
        
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        
        requirement_instance= Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        user_instance= User.objects.create(username ="username_test", password ="password_test", email ="test@test.com")
        return RequirementAuthor.objects.create(requirement= requirement_instance, author= user_instance)
    
    def test_requirement_businessrule_creation(self):
        requirement_author_instance = self.create_requirement_author()
        self.assertTrue(isinstance(requirement_author_instance, RequirementAuthor))
        self.assertEqual(requirement_author_instance.__unicode__(), requirement_author_instance.requirement_author_id)
        self.assertEqual(requirement_author_instance._meta.db_table,  'kp_req_requirement_author')          