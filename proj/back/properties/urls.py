from django.urls import path
from .views import (
    FeatureListView,
    PropertyListView, PropertyCreateView,
    PropertyRetrieveView, PropertyUpdateView, PropertyDeleteView,
)

urlpatterns = [
    path('features/', FeatureListView.as_view(), name='feature-list'),
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('properties/create/', PropertyCreateView.as_view(), name='property-create'),
    path('properties/<int:pk>/', PropertyRetrieveView.as_view(), name='property-detail'),
    path('properties/<int:pk>/update/', PropertyUpdateView.as_view(), name='property-update'),
    path('properties/<int:pk>/delete/', PropertyDeleteView.as_view(), name='property-delete'),
]
