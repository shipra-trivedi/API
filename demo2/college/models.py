from django.db import models

class employee(models.Model):
    Fullname=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    employee_id=models.IntegerField()

    def __str__(self):
      return self.Fullname