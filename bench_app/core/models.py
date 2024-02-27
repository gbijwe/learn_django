from django.db import models
from django import forms
from django.contrib.auth.hashers import make_password


ADM = "Admin"
CMP = "Company"
usr_choice = (
    (ADM, "Admin"),
    (CMP, "Company")
)

# resource_choice = (
#     ()
# )

class Users(models.Model):
    usr = models.CharField(max_length=255, blank=False)
    usr_type = models.CharField(max_length = 7, blank=False, null = True, choices=usr_choice)
    pswd = models.CharField(max_length=255, blank=False, null=True)
    # pswd = make_password(pswd)
    company_id = models.CharField(max_length = 255, blank=True)

    #Magic methodsssss - still don't know what it does, something to do with ORM Queries
    def __str__(self):
        return self.usr
    
    class Meta: 
        db_table = 'Users'
    
class Company(models.Model):
    company_id = models.CharField(max_length = 255, blank=False)
    total_resources = models.IntegerField(default=0)
    class Meta: 
        db_table = 'Company'

class Resource_Type(models.Model):
    resource_name = models.CharField(max_length=255, blank = False)
    resource_desc = models.TextField(blank=False)
    resource_type = models.CharField(max_length=255, blank=False)

    class Meta: 
        db_table = 'Resource Type'

class Resource(models.Model):
    resource = models.CharField(max_length=255, blank=False)
    # booked_by = how to put an id here...
    class Meta: 
        db_table = 'Resource'


