import datetime
from haystack import indexes
from kappa.requirements.models import Requirement
from omicron.testcases.models import TestCase


class TestCaseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,)
    description = indexes.CharField(model_attr='description', faceted=True, default=True)
    type_id = indexes.IntegerField(model_attr='type_id', faceted=False)
    test_case_id = indexes.IntegerField(model_attr='test_case_id', faceted=False, default=True)
    pub_created = indexes.DateTimeField(model_attr='date_created', faceted=True)
    state_id = indexes.IntegerField(model_attr='state_id', faceted=False)
    author_id = indexes.IntegerField(model_attr='author_id', faceted=False)

    def get_model(self):
        return TestCase

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_created__lte=datetime.datetime.now())
