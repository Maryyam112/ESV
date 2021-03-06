from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Feedback(models.Model):
    name = models.TextField(max_length=50)
    comment = models.TextField(max_length=500)



class Item(models.Model):
    video = EmbedVideoField()

class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='video/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

