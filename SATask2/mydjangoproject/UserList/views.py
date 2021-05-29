from django.shortcuts import render
from .models import UserList
from .serializers import UserSerializer
# Create your views here.

class UserCollection(viewsets.ModelViewSet):
    queryset = models.UserList.objects.all()
    serializer_class = serializers.UserSerializer