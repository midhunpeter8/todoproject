from django.db import models
# from django.utils import translation

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=256, unique=True, blank= True)

    def __str__(self):
        return self.title