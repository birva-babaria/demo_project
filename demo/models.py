from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_dob = models.DateTimeField('date published')

class junior(models.Model):
    junior_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    student_id = models.ForeignKey(student,on_delete=models.CASCADE,null=True)
