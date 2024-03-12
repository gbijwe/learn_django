from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from datetime import datetime, date

ADM = "Admin"
CMP = "Company"
usr_choice = (
    (ADM, "Admin"),
    (CMP, "Company")
)

# User creation and manager defined here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields) 

class CustomUsers(AbstractBaseUser):
    username = models.CharField(max_length=255, blank=False, unique=True, null=True)
    usr_type = models.CharField(max_length = 7, blank=False, null = True, choices=usr_choice)
    password = models.CharField(max_length=255, blank=False, null=True)
    company_id = models.CharField(max_length = 255, blank=True)

    USERNAME_FIELD = "username"
    objects = CustomUserManager()

    #Magic methodsssss - still don't know what it does, something to do with ORM Queries
    class Meta: 
        db_table = "custom_users"


    
# Resource information
class Resource_info(models.Model):

    resource_type_name = models.CharField(max_length=255, blank=False, unique=True)  # Enforce unique resource type names
    def __str__(self):
        return self.resource_type_name
    
    def get_absolute_url(self):
        return reverse('admindetailview', kwargs={'pk': self.pk})


BKD = "Booked"
AVL = "Available"
booking_choice = (
    (BKD, "Booked"),
    (AVL, "Available")
)
# Resource definition    
class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    resource_type = models.ForeignKey(Resource_info, on_delete=models.CASCADE)  
    created_by = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, null=True)
    booking_status = models.BooleanField(default=True)
    available_date = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=True, default=date.today().isoformat())
    # booking_date = models.DateField()

    def __str__(self):
        return self.resource_name
    
    def get_absolute_url(self):
        return reverse('detailview', kwargs={'pk': self.pk})


class Booking(models.Model):

    BOOKED = 'booked'
    RELEASED = 'released'
    
    STATUS_CHOICES = [
        (1, BOOKED),
        (0, RELEASED),
    ]
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)  # Resource being booked
    booked_by = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)  # User who booked the resource
    res_type = models.CharField(max_length=255, blank=True)
    available_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=date.today().isoformat())
    booking_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=date.today().isoformat())
    current_status = models.BooleanField(choices=STATUS_CHOICES, default=True)  # Assuming a string representation of the status
    # owner = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='bookings')
    release_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return f"Booking ID: {self.id} - Resource: {self.resource.resource_name} - Booked by: {self.booked_by.username}"
    
    def get_absolute_url(self):
        return reverse('listview', kwargs={'resource_id': self.resource_id})

