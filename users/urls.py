from django.urls import path
from .views import UserListView, UserDetailView, StudentListView, CreateStudent, DeleteAccount
from . import views

urlpatterns = [
    path('members/', UserListView.as_view(), name = 'members'),
    path('students/', StudentListView.as_view(), name = 'students'),
    path('members/<int:pk>/', UserDetailView.as_view(), name = 'user-detail'),
    path("addstudent/", views.CreateStudent.as_view(), name="add-student"),

    path('user/<int:pk>/delete/', DeleteAccount.as_view(), name = 'user-delete'),
]
