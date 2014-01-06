from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class PhoneNumberSerializer(serializers.ModelSerializer):
    operator = serializers.Field(source='operator.name')
    class Meta:
        model = PhoneNumber
        fields = ('phnumber', 'is_successful', 'operator','id')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'balance',)


class RechargeApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RechargeApi


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
