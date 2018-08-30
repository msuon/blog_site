from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField("post")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        timestamp_str = self.pub_date.strftime("%Y/%d/%m-%H:%M:%S")
        return "{} ({})".format(self.title, timestamp_str)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField()

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
