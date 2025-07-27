# serializers.py

from rest_framework import serializers
from .models import Property, Feature

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']
from rest_framework import serializers
from .models import Property, Feature

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']


class PropertySerializer(serializers.ModelSerializer):
    # Related fields
    features = FeatureSerializer(many=True, read_only=True)
    feature_ids = serializers.PrimaryKeyRelatedField(
        queryset=Feature.objects.all(), many=True, write_only=True, required=False
    )

    # Optional: Accept extra custom features as string list
    custom_features = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )

    class Meta:
        model = Property
        fields = [
            'id', 'name', 'address', 'price', 'description', 'area',
            'bedrooms', 'bathrooms', 'is_featured', 'property_type', 'for_type',
            'image', 'featured_image1', 'featured_image2',
            'features', 'feature_ids', 'custom_features',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # Handle feature_ids and custom_features separately
        feature_ids = validated_data.pop('feature_ids', [])
        custom_features = validated_data.pop('custom_features', [])

        # Create property instance
        property_instance = Property.objects.create(**validated_data)

        # Assign features
        property_instance.features.set(feature_ids)

        # Optionally create custom features
        for feature_name in custom_features:
            feature_obj, created = Feature.objects.get_or_create(name=feature_name)
            property_instance.features.add(feature_obj)

        return property_instance

    def update(self, instance, validated_data):
        feature_ids = validated_data.pop('feature_ids', None)
        custom_features = validated_data.pop('custom_features', [])

        # Update regular fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update features if provided
        if feature_ids is not None:
            instance.features.set(feature_ids)

        # Add any new custom features
        for feature_name in custom_features:
            feature_obj, created = Feature.objects.get_or_create(name=feature_name)
            instance.features.add(feature_obj)

        return instance

