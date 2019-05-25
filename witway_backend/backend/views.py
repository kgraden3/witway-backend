
from rest_framework import viewsets

from .serializers import *
from .models import UserDetail, Stake, Account

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user details to be viewed or edited.
    """
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class StakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stakes to be viewed or edited.
    """
    queryset = Stake.objects.all()
    serializer_class = StakeSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


