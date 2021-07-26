from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Tokenserializers(serializers.Serializer):
# class Tokenserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)

class Userserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')