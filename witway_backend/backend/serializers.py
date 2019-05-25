from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'url', 'id')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('gender', 'companions', 'address', 'occupation', 'user', 'url', 'id')


class StakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stake
        fields = ('creator', 'invitee', 'donationName', 'donationAccount', 'amountStaked', 'meetingDate', 'url', 'id')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('owner', 'accountHex', 'url', 'id')
