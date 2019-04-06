from django.urls import path
from .views import UserListView, UserDetailView, StudentListView
from . import views

urlpatterns = [
    path('members/', UserListView.as_view(), name = 'members'),
    path('students/', StudentListView.as_view(), name = 'students'),
    path('members/<int:pk>/', UserDetailView.as_view(), name = 'user-detail'),
]
