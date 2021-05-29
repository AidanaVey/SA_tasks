from rest_framework import serializers
from .models import UserList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = '__all__'