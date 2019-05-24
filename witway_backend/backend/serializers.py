from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'url', 'id')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('gender', 'address', 'occupation', 'user', 'id')


class StakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stake
        fields = ('creator', 'invitee', 'donationName', 'amountStaked', 'meetingDate', 'id')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('owner', 'accountHex', 'id')
