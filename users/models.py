from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from model_utils import Choices



class Profile(models.Model):
    STATUS = Choices('Premium', 'Basic', 'Enterprice')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    membership_type = models.CharField(choices=STATUS, default=STATUS.Basic, max_length=30)

    def __str__(self):
        return f'{self.user.username} Profile'
