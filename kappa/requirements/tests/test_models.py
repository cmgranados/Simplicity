from django.test import TestCase
from kappa.requirements.models import Requirement
from datetime import datetime


class RequirementTestCase(TestCase):
    
    def create_requirement(self):
        Requirement.objects.create(title="Req_test", description="description example", type="1", state="1", 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        
    def test_requirement_creation(self):
        requirement_instance = self.create_requirement()
        self.assertTrue(isinstance(requirement_instance, Requirement))
        self.assertEqual(requirement_instance.__unicode__(), requirement_instance.title)