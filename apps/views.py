from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters


from apps.models import Object
from apps.serializer import ObjectSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Object class
    """
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
