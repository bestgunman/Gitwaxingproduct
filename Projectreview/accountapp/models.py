from django.db import models
from django.conf import settings
import os

def get_profileimg_path(instance, filename):
	return os.path.join('profile_image', str(instance.accuser.pk), filename)

class Profile(models.Model):
	accuser = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	nickname = models.CharField(max_length = 50)
	bio = models.TextField(max_length = 100)
	profileimg = models.ImageField(blank=True, upload_to=get_profileimg_path)