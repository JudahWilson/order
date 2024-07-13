'''
Response schemas for DRF
'''
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.db import models

def get_model_fields(model_class):
    '''
    Dynamically get the fields of a model for serialization
    '''
    base_attrs = dir(models.Model)
    model_fields = [field.name for field in model_class._meta.get_fields() 
                    if field.name not in base_attrs and not field.name.startswith('_') 
                    and field.name != 'Meta']
    return model_fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']