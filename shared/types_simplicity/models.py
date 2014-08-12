from django.db import models


class TypeClassification(models.Model):
    type_classification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "adm_type_classification"


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=False)
    code = models.CharField(max_length=45, blank=False)
    type_classification = models.ForeignKey(TypeClassification)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "adm_type"
        
class TypeParentType(models.Model):
    type_parent_type_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Type , related_name='typeparenttype_typeid')
    parent_type = models.ForeignKey(Type , related_name='typeparenttype_parenttypeid')

    def __unicode__(self):
        return unicode(self.type_parent_type_id)

    class Meta:
        unique_together = (("type", "parent_type"),)
        db_table = "adm_type_parent_type"

