from django.contrib import admin
from massp.models import  Contact
from massp.models import Appointment
from massp.models import Profile
from massp.models import AdminUser
from massp.models import Invoice
from massp.models import Product



# Register your models here.
admin.site.register(AdminUser)
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Profile)
admin.site.register(Invoice)
admin.site.register(Product)
