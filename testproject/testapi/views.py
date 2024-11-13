from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer
from django.http import JsonResponse

# Create your views here.

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer