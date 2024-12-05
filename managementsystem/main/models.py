from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_nember = models.CharField(max_length=15,blank=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class GalleryImage(models.Model):
    title = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title or "Un titled Image"


class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='sermon_thumbnails/')
    document = models.FileField(upload_to='sermon_documents/', blank=True, null=True)  # Upload documents
    video_url = models.URLField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




