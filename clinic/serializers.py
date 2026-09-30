from rest_framework import serializers
from .models import Pet, Owner


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    is_classic_pet = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ['id', 'owner', 'name', 'species', 'birth_year', 'is_classic_pet']

    def get_is_classic_pet(self, obj):
        return obj.birth_year < 2020


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'name', 'phone']