from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class AdminUser(AbstractUser):
    # Add additional fields if needed
    groups = models.ManyToManyField(
        Group,
        related_name='adminuser_groups',  # Unique name for reverse relation
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='adminuser_permissions',  # Unique name for reverse relation
        blank=True
    )





class Contact(models.Model):
 name=models.CharField(max_length=122)
 email=models.EmailField(max_length=122)
 Phone=models.CharField(max_length=122)
 subject=models.CharField(max_length=122)
 Message=models.TextField()

 
 def __str__(self):
     return self.name
 

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=100)
    status=models.CharField(default='PENDING',max_length=100)
    note = models.TextField(blank=True)
   
    def __str__(self):
        return self.name
    

 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField() 
    bio = models.TextField(max_length=500, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username
    # models.py
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    customer_contact = models.CharField(max_length=15)
    invoice_no = models.CharField(max_length=20, default='INV2024001')  # Default invoice number
    invoice_date = models.DateField()
    selected_service = models.CharField(max_length=50)
    charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default charges
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default subtotal
    cgst = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default CGST
    sgst = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default SGST
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default grand total

    def __str__(self):
        return self.customer_name
# class Invoice(models.Model):
#     customer_name = models.CharField(max_length=100)
#     service_charge = models.DecimalField(max_digits=10, decimal_places=2)
#     additional_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
#     contact = models.CharField(max_length=20)
#     address = models.TextField()
#     date = models.DateField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         self.total = self.service_charge + self.additional_charge
# Create your models here.

