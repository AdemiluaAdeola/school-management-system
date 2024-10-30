from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Teacher, Student
from .serializer import TeacherSerializer, StudentSerializer

# Create your views here.
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

