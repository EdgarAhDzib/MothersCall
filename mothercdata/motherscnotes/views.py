from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, viewsets, routers, urls, status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
import sys

# Create views
from django.http import HttpResponse, Http404
from django.template import loader

# Generate table list
from django.apps import apps 
from django.contrib import admin 
from django.contrib.admin.sites import AlreadyRegistered 

# Query from database tables
from .models import Fauna, Characters, Diet, Supernatural, Flora, Tech, Nature, Chapters, Social
from .serializers import FaunaSerialize, CharactersSerialize, DietSerialize, SupernaturalSerialize, FloraSerialize, TechSerialize, NatureSerialize, ChaptersSerialize, SocialSerialize

class CategMenu(APIView):
	def get(self, request):
		db_tables = apps.get_app_config('motherscnotes').get_models()
		db_tables = list(db_tables)
		db_table_names = []
		for table_n in db_tables:
			db_table_names.append(table_n.__name__)
		return Response({"names":db_table_names})

class Categs:
	model = ""
	serial = ""
	def __init__(self, name):
		self.name = name

fauna = Categs("fauna")
fauna.model = Fauna
fauna.serial = FaunaSerialize

characters = Categs("characters")
characters.model = Characters
characters.serial = CharactersSerialize

diet = Categs("diet")
diet.model = Diet
diet.serial = DietSerialize

supernatural = Categs("supernatural")
supernatural.model = Supernatural
supernatural.serial = SupernaturalSerialize

flora = Categs("flora")
flora.model = Flora
flora.serial = FloraSerialize

tech = Categs("tech")
tech.model = Tech
tech.serial = TechSerialize

nature = Categs("nature")
nature.model = Nature
nature.serial = NatureSerialize

chapters = Categs("chapters")
chapters.model = Chapters
chapters.serial = ChaptersSerialize

social = Categs("social")
social.model = Social
social.serial = SocialSerialize

class ViewAll(APIView):
	def get(self, request, categ):
		all_items = globals()[categ]
		query = all_items.model.objects.all()
		serializer = all_items.serial(query, many=True)
		return Response(serializer.data)

# REDO upsert: update_or_create is throwing 'id' errors
class ItemPost(APIView):
	def post(self, request, _id, categ):
		categ_class = globals()[categ]
		item_single = categ_class.model.objects.get(pk=_id)
		serializer = categ_class.serial(item_single, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemAdd(APIView):
	def post(self, request, categ):
		categ_class = globals()[categ]
		serializer = categ_class.serial(data=request.data)
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

class TableFields(APIView):
	def get(self, request, categ):
		categ_class = globals()[categ]
		table_fields = []
		for f in categ_class.model._meta.get_fields():
			print(f.name)
			table_fields.append(f.name)
		return Response(table_fields)

def index(request):
    return HttpResponse("First notes for Mother's Call.")

def tables(request):
    return HttpResponse("Database tables")
