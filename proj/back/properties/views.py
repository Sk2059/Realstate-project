from rest_framework import generics
from .models import Property, Feature
from .serializers import PropertySerializer, FeatureSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all().order_by('-created_at')
    serializer_class = PropertySerializer
    


class PropertyCreateView(generics.CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
   


class PropertyRetrieveView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    


class PropertyUpdateView(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    


class PropertyDeleteView(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    

class FeatureListView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
   