from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=140, default='description')
    image = models.ImageField(default='default.jpg', upload_to='food_pics')
    ingredients = models.TextField(max_length=140, default='ingredients')
    method = models.TextField(max_length=140, default='method')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
