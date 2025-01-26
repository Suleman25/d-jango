from rest_framework import serializers
from .models import Teacher , Student
class TeacherSerializer(serializers.ModelSerializer):
    class meta:
        model = Teacher
        fields = '__all__'

        def create (self , validated_data):
            teacher = Teacher.objects.create_teacher(** validated_data)
            return teacher

class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class meta:
        model = Student
        fields = '__all__'