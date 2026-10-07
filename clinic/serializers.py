from rest_framework import serializers
from .models import Owner, Pet, MedicalRecord
from datetime import datetime


class OwnerSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Owner
        fields = ['id', 'user', 'user_name', 'name', 'phone']


class PetSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.name', read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'owner', 'owner_name', 'name', 'species', 'birth_year']

    def validate_birth_year(self, value):
        current_year = datetime.now().year
        if value < 2000:
            raise serializers.ValidationError('Animal can\'t be that old and still living')
        if value > current_year:
            raise serializers.ValidationError('Year of birth can\'t be from future')
        return value


class MedicalRecordSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source='pet.name', read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'pet', 'pet_name', 'diagnosis', 'treatment', 'date_created', 'cost']

    def validate(self, data):
        diagnosis = data.get('diagnosis', '').lower()
        cost = data.get('cost', 0)

        if cost > 5000 and 'check-up' in diagnosis:
            raise serializers.ValidationError(
                'A regular check-up cannot cost more than 5000 UAH.'
                ' Please check the diagnosis or the cost.')
        return data