from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

ADM = "Admin"
CMP = "Company"
usr_choice = (
    (ADM, "Admin"),
    (CMP, "Company")
)

# Create your models here.

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
