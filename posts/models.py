from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, db_column="user", default=1)
    image = models.FileField(upload_to='media', blank=True)
    body = HTMLField()

    def __str__(self):
        print(self.pub_date)
        return str(self.title + "  " + self.pub_date.strftime("%Y-%m-%d"))