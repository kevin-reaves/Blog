from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import time
import os





# Create your models here.
class Post(models.Model):

    #renames images with a timestamp, avoids diplicate names
    def get_upload_to(self, filename):
        filename, file_extension = os.path.splitext(filename)
        timestamp = 'media/%f' % time.time()
        return str(timestamp + file_extension)

    def __str__(self):
        print(self.pub_date)
        return str(self.title + "  " + self.pub_date.strftime("%Y-%m-%d"))


    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, db_column="user", default=1)
    #ImageField is currently not filtering non-images like it should.
    #A temporary band aid has been applied on the HTML side.
    image = models.ImageField(upload_to=get_upload_to, blank=True, default="media/defaultBlogImage.png")
    body = HTMLField()