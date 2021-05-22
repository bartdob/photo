from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile

class Photo(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(default='photo/default.jpg', upload_to='photo')
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('photo-detail', kwargs={'pk': self.pk})