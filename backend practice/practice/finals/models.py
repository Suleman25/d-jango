from django.db import models

class Teacher (models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student ( models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher , on_delete = models.CASCADE , related_name= 'sir')   
     
    def __str__(self):
        return self.name