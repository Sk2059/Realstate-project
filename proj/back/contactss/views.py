from rest_framework import generics
from .models import ContactMessage, ServiceRequest,Sell
from .serializers import ContactMessageSerializer, ServiceRequestSerializer, SellSerializer
from rest_framework.response import Response
from rest_framework import status


class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    


class ContactMessageListView(generics.ListAPIView):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    


class ContactMessageDetailView(generics.RetrieveAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    

class ContactMessageDeleteView(generics.DestroyAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    

class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all().order_by('-created_at')
    serializer_class = ServiceRequestSerializer
    

class ServiceRequestDeleteView(generics.DestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    lookup_field = 'id'
   
    
    

class SellListCreateView(generics.ListCreateAPIView):
    queryset = Sell.objects.all().order_by('-id')
    serializer_class = SellSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)  # <-- Debug line
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class SellDeleteView(generics.DestroyAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    lookup_field = 'id'

