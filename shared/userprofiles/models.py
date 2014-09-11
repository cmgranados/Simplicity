from django.db import models
from django.contrib.auth.models import User
from shared.types_simplicity.models import Type


# Create your models here.
class UserProfile(models.Model):
    '''
    Extension of the User Model
    '''
    user = models.OneToOneField(User)
    registration_type = models.ForeignKey(Type)

    class Meta:
        db_table = "adm_user_profile"
