from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, viewsets, routers, urls, status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
import sys

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

# Query from database tables
from .models import Fauna
from .serializers import FaunaSerialize

class FaunaAPI(APIView):
	def get(self, request):
		fauna_test = Fauna.objects.all()
		serializer = FaunaSerialize(fauna_test, many=True)
		return Response(serializer.data)

# REDO upsert: update_or_create is throwing 'id' errors
class FaunaPost(APIView):
	def post(self, request, fauna_id):
		fauna_single = Fauna.objects.get(pk=fauna_id)
		serializer = FaunaSerialize(fauna_single, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FaunaAdd(APIView):
	def post(self, request):
		serializer = FaunaSerialize(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FaunaItem(APIView):
	def get(self, request, fauna_id):
		fauna_single = Fauna.objects.get(pk=fauna_id)
		serializer = FaunaSerialize(fauna_single)
		return Response(serializer.data)

class FaunaDelete(APIView):
	def delete(self, request, fauna_id):
		fauna_single = Fauna.objects.get(pk=fauna_id)
		fauna_single.delete()
		return Response({"message":"deleted"}, status=status.HTTP_200_OK)

def index(request):
    return HttpResponse("First notes for Mother's Call.")

def tables(request):
    return HttpResponse("Database tables")
