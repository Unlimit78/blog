from django.urls import reverse
from django.views.generic import ListView,DetailView,View
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog,Post,User


class PostListView(LoginRequiredMixin,ListView):
    context_object_name = "subscribed"

    template_name = "index.html"
    def get_queryset(self):
        user = self.request.user

        return user.subscribed.all

    def post(self,request):
        user = self.request.user
        post = Post.objects.get(pk=request.POST.get('pk'))
        user.is_readed.add(post)
        return HttpResponseRedirect(reverse('index'))

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)

        context['user'] = user
        return context

class BlogListView(LoginRequiredMixin,ListView):
    queryset = Blog.objects.all()
    context_object_name = "blogs"
    template_name = 'blogs.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)

        context['user'] = user
        return context

    def post(self,request):
        user = self.request.user
        blog = Blog.objects.get(pk=request.POST.get('pk'))
        if blog in user.subscribed.all():
            user.subscribed.remove(blog)
            for post in blog.posts.all():
                user.is_readed.remove(post)
        else:
            user.subscribed.add(blog)
        return HttpResponseRedirect(reverse('blogs'))

class UserLogin(LoginView):
    template_name = 'login.html'

class UserLogout(LoginRequiredMixin,LogoutView):
    template_name = 'logout.html'
