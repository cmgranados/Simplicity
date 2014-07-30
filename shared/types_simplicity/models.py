from django.db import models


class TypeClassification(models.Model):
    type_classification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=False)
    code = models.CharField(max_length=45, blank=False)
    type_classification_id = models.ForeignKey(TypeClassification)
    parent_type_id = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
