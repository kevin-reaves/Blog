from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = HTMLField()

    def __str__(self):
        print(self.pub_date)
        return str(self.title + "  " + self.pub_date.strftime("%Y-%m-%d"))