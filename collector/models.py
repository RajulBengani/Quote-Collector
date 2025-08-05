from django.db import models

# Create your models here.
class Quote(models.Model):
    quote=models.CharField(max_length=200)
    author=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'"{self.quote}"- {self.author}'