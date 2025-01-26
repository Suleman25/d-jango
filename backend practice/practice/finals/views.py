from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher , Student
from rest_framework.permissions import IsAuthenticated
from .serializers import TeacherSerializer , StudentSerializer


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]    