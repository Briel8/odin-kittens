from django.db import models

class Kitten(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    cuteness = models.CharField(max_length=50)
    softness = models.CharField(max_length=50)

    def __str__(self):
        return self.name