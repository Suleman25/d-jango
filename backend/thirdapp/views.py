from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, StudentSerializer
from .models import book , Student
from rest_framework.filters import OrderingFilter

# Create your views here.
class bookView(generics.ListAPIView):
    serializer_class = BookSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    queryset = book.objects.all()


class createView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = book.objects.all()    

class retrieveView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = book.objects.all() 
    lookup_field=id 

class deleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = book.objects.all() 
    lookup_field=id         

class studentView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()    