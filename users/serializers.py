from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User

# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nom', 'email', 'phone_number', 'wilaya', 'commune', 'date_of_birth']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Email ou mot de passe incorrect.")

        attrs["user"] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id", "nom", "username", "email", "phone_number",
            "wilaya", "commune", "password", "confirm_password", "date_of_birth",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        if not attrs["phone_number"].startswith("0"):
            raise serializers.ValidationError("Le numéro doit commencer par 0.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
