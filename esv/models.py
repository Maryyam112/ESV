from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.TextField()
    comment = models.TextField()


class Videos(models.Model):
    id = models.IntegerField()
    title = models.TextField()
