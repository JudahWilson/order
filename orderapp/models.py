from django.db import models, transaction
from django.dispatch import receiver
from django.db.models.signals import pre_save


# Create your models here.
from custom_user.models import AbstractEmailUser

class OrderUser(AbstractEmailUser):
    '''
    Custom user class
    '''
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    pass


class Organization(models.Model):
    '''
    Organization using application
    '''
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    territory = models.CharField(max_length=60,blank=True)
    country = models.CharField(max_length=60,blank=True)
    postal_code = models.CharField(max_length=15,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    phone_extension = models.CharField(max_length=8,blank=True)
    email = models.EmailField(max_length=100)
    domain = models.CharField(max_length=100,blank=True) # email domain of all users of the org
    website = models.URLField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='organization_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='organization_updated_by',blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    '''
    Contacts
    '''
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60,blank=True)
    last_name = models.CharField(max_length=60,blank=True)
    title = models.CharField(max_length=60,blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15,blank=True)
    phone_extension = models.CharField(max_length=8,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='contact_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='contact_updated_by',blank=True)

    def __str__(self):
        return self.email
    
    
class Account(models.Model):
    '''
    Account (often a company customer of org)
    '''
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='account_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='account_updated_by',blank=True)

    def __str__(self):
        return self.name
    
    
class Ticket(models.Model):
    '''
    Tickets
    '''
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    ticket_number = models.IntegerField(blank=True, null=True) # TODO see chatgpt for auto increment per org id
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Contact, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=60)
    priority = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='ticket_created_by')
    updated_by = models.ForeignKey(OrderUser, on_delete=models.CASCADE, related_name='ticket_updated_by')

    class Meta:
        unique_together = ('organization', 'ticket_number')
    
    def __str__(self):
        return self.title
    

class OrgTicketCounter(models.Model):
    '''
    Counter for latest ticket number per organization
    '''
    orgid = models.IntegerField(primary_key=True)
    last_ticket_number = models.IntegerField(default=0)
    

@receiver(pre_save, sender=Ticket)
def set_ticket_number(sender, instance, **kwargs):
    if instance.pk is None:  # Only set ticket number for new records
        with transaction.atomic():
            counter, created = OrgTicketCounter.objects.select_for_update().get_or_create(orgid=instance.organization.id)
            counter.last_ticket_number += 1
            instance.ticket_number = counter.last_ticket_number
            counter.save()
'''
Linking Tables
'''