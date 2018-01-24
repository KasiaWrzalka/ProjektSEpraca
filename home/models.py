from django.db import models

# Create your models here.

class Tests(models.Model):
    title = models.CharField(max_length=8000)
    description = models.CharField(max_length=8000)

    def __str__(self):
        return self.title

class Questions(models.Model):
    title = models.CharField(max_length=8000)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
