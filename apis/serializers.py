from rest_framework import serializers

# Import the models from models.py
from .models import Car, Dealer, Sales

# Create a model serializer for the Car model
class CarSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialization
    class Meta:
        model = Car
        fields = ('name', 'description')

# Create a model serializer for the Dealer model
class DealerSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialization
    class Meta:
        model = Dealer
        fields = ('name', 'description')

# Create a model serializer for the Sales model
class SalesSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialization
    class Meta:
        model = Sales
        fields = ('car', 'dealer', 'description', 'created_at')
