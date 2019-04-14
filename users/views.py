from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from blog.models import Post
from groups.models import Group, GroupMember
from .models import Profile, Student
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Account Creation Successful! You can login now')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, 'title':'Registration',})

@login_required
def profile(request):
    context = {
        'posts' : Post.objects.all(),
        'groups' : Group.objects.all(),
        'title' : 'Profile',
    }
    return render(request, 'users/profile.html', context)



@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Update Successful!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'posts' : Post.objects.all(),
        'title' : 'Edit Profile',
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request, 'users/editprofile.html', context)

@login_required
def members(request):
    context = {
        'profiles' : User.objects.all(),
        #'posts' : Post.objects.all(),
        'title' : 'Members',

        #Project.objects.values('informationunit__username').distinct().count()
    }
    return render(request, 'users/members.html', context)


class UserListView(LoginRequiredMixin, ListView):
    model = Profile
    #template_name = 'user/members.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'profiles' #use post.author instead of object.author
    ordering = ['user']
    paginate_by = 10 #buit in paginator function

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'users/students.html'
    ordering = ['id']
    paginate_by = 20

class CreateStudent(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    #form_class = forms.PostForm
    fields = ('name','id', 'email')
    model = Student
    success_url = reverse_lazy("students")

    def test_func(self):
        return self.request.user.is_staff



class UserDetailView(LoginRequiredMixin, DetailView):
    model = Profile
