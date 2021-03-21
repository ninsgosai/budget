from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class AdminauthModel(models.Model):
    id = models.AutoField(primary_key=True)
    admin_email = models.EmailField(max_length=255)
    admin_password = models.CharField(max_length=255)
    profile_pic = models.ImageField('Profile Pic', upload_to='profile_pic/',null=True)
    created_date = models.DateTimeField(auto_now_add=True)

