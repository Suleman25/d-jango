from django.db import models

# Create your models here.
class book (models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll= models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.roll

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    # student= models.ForeignKey(Student,on_delete=models.CASCADE)
    # student= models.ManyToManyField(Student)
    student= models.OneToOneField(Student,on_delete=models.CASCADE,related_name='assignment',default='st')

    def __str__(self):
        return self.name   