from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, viewsets, routers, urls, status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# Query from database tables
from .models import Fauna
from .serializers import FaunaSerialize

class FaunaAPI(APIView):
	def get(self, request):
		fauna_test = Fauna.objects.all()
		serializer = FaunaSerialize(fauna_test, many=True)
		return Response(serializer.data)
	
	def post(self):
		pass

def index(request):
    return HttpResponse("First notes for Mother's Call.")

def tables(request):
    return HttpResponse("Database tables")
