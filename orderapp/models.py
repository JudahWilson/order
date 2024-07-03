from django.db import models

# Create your models here.
from custom_user.models import AbstractEmailUser

class OrderUser(AbstractEmailUser):
    '''
    Custom user class
    '''
    pass


class Organization(models.Model):
    '''
    Organization class
    '''
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    territory = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    phone_extension = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='organization_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='organization_updated_by')

    def __str__(self):
        return self.name

class Contact(models.Model):
    '''
    Contact class
    '''
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    phone_extension = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='contact_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='contact_updated_by')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
class Account(models.Model):
    '''
    Account class
    '''
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='account_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='account_updated_by')

    def __str__(self):
        return self.name
    
    
class Ticket(models.Model):
    '''
    Ticket class
    '''
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=60)
    priority = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='ticket_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='ticket_updated_by')

    def __str__(self):
        return self.title