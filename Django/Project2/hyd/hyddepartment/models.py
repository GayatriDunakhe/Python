from django.db import models

class Infyx(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.bio}"