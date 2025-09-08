from django.db import models
from PIL import Image

def upload_image(instance, filename):
    return f'media/itservices/{filename}'

# Create your models here.
class ItServices(models.Model):
    display = models.BooleanField(default=True)

    tags = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_image)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the original image first
        img = Image.open(self.image.path)
        max_width = 250
        if img.width > max_width:
            aspect_ratio = img.height / img.width
            new_height = int(max_width * aspect_ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            img.save(self.image.path)

class UserQueries(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return self.name

class FAQs(models.Model):
    display = models.BooleanField(default=False)

    question = models.CharField(max_length=300)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.question[:10] + '...'