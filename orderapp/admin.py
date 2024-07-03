from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import *

# Register your models here.
class OrderUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    pass

admin.site.register(
    OrderUser,
    OrderUserAdmin,
)

admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(Account)
admin.site.register(Ticket)