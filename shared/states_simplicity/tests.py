
from django.test import TestCase

from shared.states_simplicity.models import State, StateType


# MODELS
class StateTestCase(TestCase):
    
    def create_state(self):
        state_type_instance = StateType.objects.create(name="state_type_name", description="state_type_description")
        return State.objects.create(name="state_name", description="state_description",
                                     state_type=state_type_instance, )
        
    def test_state_creation(self):
        state_instance = self.create_state()
        self.assertTrue(isinstance(state_instance, State))
        self.assertEqual(state_instance.__unicode__(), state_instance.name)
        self.assertEqual(state_instance._meta.db_table,  'adm_state')

class StateTypeTestCase(TestCase):
    
    def create_state_type(self):
        return StateType.objects.create(name="state_type_name", description="state_type_description")
        
    def test_state_type_creation(self):
        state_type_instance = self.create_state_type()
        self.assertTrue(isinstance(state_type_instance, StateType))
        self.assertEqual(state_type_instance.__unicode__(), state_type_instance.name)
        self.assertEqual(state_type_instance._meta.db_table,  'adm_state_type')
