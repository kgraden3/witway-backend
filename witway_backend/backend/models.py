import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    companions = models.ForeignKey('UserDetail', on_delete=models.PROTECT, related_name='companions', null=True)


class UserDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Stake(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invitee")
    donationName = models.CharField(max_length=100)
    donationAccount = models.CharField(max_length=100)
    amountStaked = models.DecimalField(decimal_places=6, max_digits=10)
    meetingDate = models.DateTimeField()


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    accountHex = models.CharField(max_length=42)
