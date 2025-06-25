from django.db import models

# Create your models here.
class Contact(models.Model):
    FullName = models.CharField(max_length=30)
    Email = models.EmailField()
    YourMessage = models.TextField()

    def __str__(self):
        return self.FullName
