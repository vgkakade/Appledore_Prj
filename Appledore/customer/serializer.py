from rest_framework import serializers
from .models import Customer, Address
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)

        token['firstname'] = user.first_name
        return token


class UserSerializer(serializers.ModelSerializer):
    mobile_number = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name','last_name','email','mobile_number']

    def get_mobile_number(self, obj):
        try:
            obj = Customer.objects.get(user=obj.id)
        except Customer.DoesNotExist:
            return ""


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('customer',)