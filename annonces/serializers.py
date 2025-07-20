from rest_framework import serializers
from .models import Category , Announce
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class AnnounceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = serializers.StringRelatedField()  # pour afficher le nom de la catégorie

    class Meta:
        model = Announce
        fields = ['id', 'category', 'user', 'description', 'prix', 'prix_mode', 'image', 'specification']