from datetime import datetime

from django.test import TestCase

from shared.states_simplicity.models import State, StateType
from shared.types_simplicity.models import Type, TypeClassification
from kappa.businessrules.models import BusinessRule


# MODELS
class BusinessRuleTestCase(TestCase):
    
    def create_business_rule(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved)
        return BusinessRule.objects.create(name="Req_test", description="description example", type=type_retrieved, state_type=state_retrieved,
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123")
        
    def test_business_rule_creation(self):
        business_rule_instance = self.create_business_rule()
        self.assertTrue(isinstance(business_rule_instance, BusinessRule))
        self.assertEqual(business_rule_instance.__unicode__(), business_rule_instance.name)
        self.assertEqual(business_rule_instance._meta.db_table, 'kp_br_business_rule')
