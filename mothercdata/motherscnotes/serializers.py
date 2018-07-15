from rest_framework import serializers
from .models import Fauna

class FaunaSerialize(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model=Fauna
		# fields=('id','name','classification','indigenous','image','notes')
		fields = '__all__'
