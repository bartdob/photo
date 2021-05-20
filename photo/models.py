from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(default='photo/default.jpg', upload_to='photo')
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title