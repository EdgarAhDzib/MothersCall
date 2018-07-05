from rest_framework import serializers
from .models import Fauna

class FaunaSerialize(serializers.ModelSerializer):
	class Meta:
		model=Fauna
		# fields=('name','classification','indigenous','image','notes')
		fields = '__all__'
