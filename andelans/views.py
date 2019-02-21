from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Andelan
from .serializers import AndelansSerializer

# Create your views here.


class AndelansListView(generics.ListAPIView):
    queryset = Andelan.objects.all()
    serializer_class = AndelansSerializer