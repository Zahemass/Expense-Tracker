from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AddItemSerializer
from .models import AddItems

# Create your views here.
class AddView(viewsets.ModelViewSet):
    serializer_class = AddItemSerializer
    queryset = AddItems.objects.all()
