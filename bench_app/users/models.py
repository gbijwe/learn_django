from django.db import models
from django.contrib.auth.models import AbstractUser
ADM = "Admin"
CMP = "Company"
usr_choice = (
    (ADM, "Admin"),
    (CMP, "Company")
)

# Create your models here.
class Users(AbstractUser):
    pass
    usr = models.CharField(max_length=255, blank=False, unique=True, null=True)
    usr_type = models.CharField(max_length = 7, blank=False, null = True, choices=usr_choice)
    pswd = models.CharField(max_length=255, blank=False, null=True)
    company_id = models.CharField(max_length = 255, blank=True)
    
    #Magic methodsssss - still don't know what it does, something to do with ORM Queries
    # USERNAME_FIELD = "usr"

    def __str__(self):
        return self.usr