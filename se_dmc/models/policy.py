from django.db import models


class Policy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='policy/')

    def __str__(self):
        return self.title




