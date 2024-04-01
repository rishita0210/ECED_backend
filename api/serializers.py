from django.contrib.auth.models import Group, User 
from api.models import Student
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ 'first_name', 'last_name', 'age', 'email', 'created_at','marks']
