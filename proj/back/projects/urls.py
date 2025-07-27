from django.urls import path
from .views import (
    ProjectListView, ProjectCreateView, ProjectRetrieveView, ProjectUpdateView, ProjectDeleteView,
  
)


urlpatterns = [
    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectRetrieveView.as_view(), name='project-retrieve'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
