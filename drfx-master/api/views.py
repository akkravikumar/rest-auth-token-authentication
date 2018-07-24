from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class ProfileView(APIView):
	def get(self, request, format=None):
		return Response("{token:toeken}",status=status.HTTP_200_OK)