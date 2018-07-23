from rest_framework import serializers
from .models import Fauna, Characters, Diet, Supernatural, Flora, Tech, Nature, Chapters, Social

class FaunaSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Fauna
		fields = '__all__'

class CharactersSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Characters
		fields = '__all__'

class DietSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Diet
		fields = '__all__'

class SupernaturalSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Supernatural
		fields = '__all__'

class FloraSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Flora
		fields = '__all__'

class TechSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Tech
		fields = '__all__'

class NatureSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Nature
		fields = '__all__'

class ChaptersSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Chapters
		fields = '__all__'

class SocialSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Social
		fields = '__all__'
