from django.urls import path
from .views import UserListView, UserDetailView, StudentListView, CreateStudent, DeleteAccount
from . import views

urlpatterns = [
    path('members/', UserListView.as_view(), name = 'members'),
    path('students/', StudentListView.as_view(), name = 'students'),
    path('students/<int:pk>/update/', views.UpdateStudent.as_view(), name = 'student-update'),
    path("addstudent/", views.CreateStudent.as_view(), name="add-student"),

    path('members/<int:pk>/', UserDetailView.as_view(), name = 'user-detail'),
    path('user/<int:pk>/delete/', DeleteAccount.as_view(), name = 'user-delete'),
]
