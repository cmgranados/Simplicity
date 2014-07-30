from django.db import models


class TypeClassification(models.Model):
    type_classification = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "adm_type_classification"


class Type(models.Model):
    type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=False)
    code = models.CharField(max_length=45, blank=False)
    type_classification = models.ForeignKey(TypeClassification)
    parent_type = models.ForeignKey('self', related_name='parent_type_id')

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "adm_type"
