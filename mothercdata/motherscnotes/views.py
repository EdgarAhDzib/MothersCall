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

class Categs:
	model = ""
	serial = ""
	def __init__(self, name):
		self.name = name

fauna = Categs("fauna")
fauna.model = Fauna
fauna.serial = FaunaSerialize

class ViewAll(APIView):
	def get(self, request, categ):
		print(categ)
		all_items = globals()[categ]
		query = all_items.model.objects.all()
		serializer = all_items.serial(query, many=True)
		return Response(serializer.data)

# REDO upsert: update_or_create is throwing 'id' errors
class FaunaPost(APIView):
	def post(self, request, _id):
		fauna_single = Fauna.objects.get(pk=_id)
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

class GetItem(APIView):
	def get(self, request, _id, categ):
		categ_class = globals()[categ]
		item_single = categ_class.model.objects.get(pk=_id)
		serializer = categ_class.serial(item_single)
		return Response(serializer.data)

class ItemDelete(APIView):
	def delete(self, request, _id, categ):
		categ_class = globals()[categ]
		item_single = categ_class.model.objects.get(pk=_id)
		item_single.delete()
		return Response({"message":"deleted"}, status=status.HTTP_200_OK)

def index(request):
    return HttpResponse("First notes for Mother's Call.")

def tables(request):
    return HttpResponse("Database tables")
