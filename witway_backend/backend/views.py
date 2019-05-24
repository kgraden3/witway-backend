
from rest_framework import viewsets

from .serializers import *
from .models import UserDetails, Stake, Account
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user details to be viewed or edited.
    """
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer


class StakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user details to be viewed or edited.
    """
    queryset = Stake.objects.all()
    serializer_class = StakeSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user details to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
