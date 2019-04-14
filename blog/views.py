from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . models import Post
from groups.models import Group
from users.models import Student

def index(request):
    context = {
        'posts' : Post.objects.all(),
        'groups' : Group.objects.all(),
        'title' : 'Index',
    }
    return render(request, 'blog/index.html', context)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #use post.author instead of object.author
    ordering = ['-date_posted'] #for ordering accoing to date
    paginate_by = 15 #buit in paginator function

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False
    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted from database")
        return super().delete(*args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] #form fields

    def form_valid(self, form):
        #form<this form> <set author> = current logged in user
        form.instance.author = self.request.user
        #run overridden form_valid method
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] #form fields

    def form_valid(self, form):
        #form<this form> <set author> = current logged in user
        #form.instance.author = self.request.user
        #run overridden form_valid method
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False

    def update(self, *args, **kwargs):
        messages.success(self.request, "Post Updated!")
        return super().update(*args, **kwargs)



def about(request):
    context = {
        'title' : 'About',
    }
    return render(request, 'blog/about.html', context)

def newsfeed(request):
    num = Student.objects.filter(email = "faruqui").count()
    context = {
        'posts' : Post.objects.all(),
        'num' : num,
        'students' : Student.objects.all(),
        #'posts' : Post.objects.filter(author = {{ user }}),
        'title' : 'Newsfeed',
    }
    return render(request, 'blog/newsfeed.html', context)
