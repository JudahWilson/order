from django.db import models

# Create your models here.
from custom_user.models import AbstractEmailUser

class OrderUser(AbstractEmailUser):
    '''
    Custom user class
    '''
    pass