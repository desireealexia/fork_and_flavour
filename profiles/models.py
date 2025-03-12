from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    def save(self):
        super().save()

        img = Image.open(self.profile_picture.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.profile_picture.path) # Save it again and override the larger image