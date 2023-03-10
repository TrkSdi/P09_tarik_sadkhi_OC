from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Nom d'utilisateur obligatoire")
        user = self.model(username=username,)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self.db)
        
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=10,
        unique=True,
        blank=False
    )
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    
    def __str__(self):
        return f"{self.username}"
        
    
    
    USERNAME_FIELD = "username"
    
