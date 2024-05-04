from django.db import models

# Create your models here.
""" 
POST Class
"""


class POST(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    createdAT = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
