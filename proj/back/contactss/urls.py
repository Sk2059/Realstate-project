from django.urls import path
from .views import (
    ContactMessageCreateView,
    ContactMessageListView,
    ContactMessageDetailView,
    ContactMessageDeleteView,
    ServiceRequestListCreateView, ServiceRequestDeleteView,
    SellListCreateView, SellDeleteView
)

urlpatterns = [
    path('messages/', ContactMessageListView.as_view(), name='message-list'),
    path('messages/create/', ContactMessageCreateView.as_view(), name='message-create'),
    path('messages/<int:pk>/', ContactMessageDetailView.as_view(), name='message-detail'),
    path('messages/<int:pk>/delete/', ContactMessageDeleteView.as_view(), name='message-delete'),

    path('service-requests/', ServiceRequestListCreateView.as_view(), name='service-request-list-create'),
    path('service-requests/<int:id>/delete/', ServiceRequestDeleteView.as_view(), name='service-request-delete'),

    path('sell/', SellListCreateView.as_view(), name='sell-list-create'),
    path('sell/<int:id>/delete/', SellDeleteView.as_view(), name='sell-delete'),
]
