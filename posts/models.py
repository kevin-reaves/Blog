from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import time


# Create your models here.
class Post(models.Model):

    #renames images with a timestamp, avoids diplicate names
    def get_upload_to(instance, filename):
        return 'media/%f.jpg' % time.time()

    def __str__(self):
        print(self.pub_date)
        return str(self.title + "  " + self.pub_date.strftime("%Y-%m-%d"))

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, db_column="user", default=1)
    image = models.FileField(upload_to=get_upload_to, blank=True, default="media/defaultBlogImage.png")
    body = HTMLField()



