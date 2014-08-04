from rest_framework import serializers
from kappa.businessrules.models import BusinessRule

class BusinessRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessRule
        fields = ('business_rule_id', 'name', 'description')
    