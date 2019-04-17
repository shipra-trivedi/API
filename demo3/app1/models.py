from django.db import models

class language(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    Language_known=models.CharField(max_length=20)
    scale=models.IntegerField()

    def __src__(self):
        return self.name

