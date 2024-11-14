from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import *
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[AllowAny]

class CeateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer 
    permission_classes = [AllowAny]

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self,request):
        user = self.request.user
        return Note.objects.filter(author=user)
    


