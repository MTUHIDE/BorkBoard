from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Create your models here.

upload_directory = 'account/profilepics/'

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=50, blank = True, null=True)
    home_city = models.CharField(max_length=50, blank = True, null=True)
    home_state = models.CharField(max_length=50, blank = True, null=True)
    zipcode = models.IntegerField(blank = True, null=True)
    picture = models.ImageField(upload_to=upload_directory, height_field=None, width_field=None, blank = True, null=True)

@receiver(pre_save, sender=user_profile)
def delete_changed_photos(sender, instance, **kwargs):
    try:
        user = user_profile.objects.get(pk=instance.pk)
    except user_profile.DoesNotExist:
        pass #
    if not instance.picture == user.picture:
        user.picture.delete(save=False)


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile.objects.create(user=instance)

class UserInLine(admin.StackedInline):
    model = user_profile
    can_delete = False
    verbose_name_plural = 'user_profile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
