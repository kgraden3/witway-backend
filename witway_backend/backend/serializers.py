from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'url')

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('gender','address','occupation','user')

class StakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stake
        fields = ('creator','invitee','donationName','amountStaked')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('owner','accountHex')
