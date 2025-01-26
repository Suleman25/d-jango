from rest_framework import serializers
from .models import book , Student

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book 
        fields = ['id','name','author','price']
        # fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['name' , 'roll']
