from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        print("nkdjskd")
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"