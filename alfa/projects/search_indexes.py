import datetime
from haystack import indexes
from kappa.requirements.models import Requirement
from alfa.projects.models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,)
    description = indexes.CharField(model_attr='description', faceted=True, default=True)
    name = indexes.CharField(model_attr='name', faceted=True, default=True)
    project_id = indexes.CharField(model_attr='project_id', faceted=False, default=True)
    pub_created = indexes.DateTimeField(model_attr='date_created', faceted=True)

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_created__lte=datetime.datetime.now())
