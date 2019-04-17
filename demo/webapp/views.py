from django.shortcuts import render
from rest_framework import viewsets
from .models import student
from .serializers import studentSerializer

class studentView(viewsets.ModelViewSet):
        queryset = student.objects.all()
        serializer_class = studentSerializer
