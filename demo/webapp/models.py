from django.db import models

class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    student_id=models.IntegerField()

    def __src__(self):
        return self.firstname
