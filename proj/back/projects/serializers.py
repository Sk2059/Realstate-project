from rest_framework import serializers
from .models import Project, Feature, Challenge, projimage, Outcome

class ProjectSerializer(serializers.ModelSerializer):
    features = serializers.SlugRelatedField(
        many=True, slug_field='name', read_only=True
    )
    challenges = serializers.SlugRelatedField(
        many=True, slug_field='name', read_only=True
    )
    outcomes = serializers.SlugRelatedField(
        many=True, slug_field='outcome', read_only=True
    )
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_image_urls(self, obj):
        try:
            return [img.img.url for img in obj.images.all()]
        except Exception as e:
            print(f"Error getting image URLs: {e}")
            return []
