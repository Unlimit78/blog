from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import ListView,DetailView,FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog,Post,User
from .forms import PostForm

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

class PostCreateView(LoginRequiredMixin,FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        post = form.save()
        self.request.user.blog.posts.add(post)
        self.send_mail(post)
        return super(PostCreateView, self).form_valid(form)
    def send_mail(self,post):
        subject = 'New post'
        message = "Hey new post !"
        html_content = '<a href="{}">Click here</a>'.format(post.get_absolute_url())
        emails = []
        for user in User.objects.all():
            if self.request.user.blog in user.subscribed.all():
                emails.append(user.email)
        msg = EmailMultiAlternatives(subject,message,'your_account@gmail.com',emails)
        msg.attach_alternative(html_content,'text/html')
        msg.send()

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

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
