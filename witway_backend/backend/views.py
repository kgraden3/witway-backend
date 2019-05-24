from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework import viewsets

from .serializers import UserSerializer


# class CreateUserView(CreateAPIView):
#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny  # Or anon users can't register
#     ]
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
