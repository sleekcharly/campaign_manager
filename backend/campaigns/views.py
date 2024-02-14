from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class CampaignListAPIView(generics.ListAPIView):
    
    def get_queryset(self):
        return 