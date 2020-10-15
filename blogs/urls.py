from django.urls import path,include

from .views import PostListView,UserLogin,UserLogout,BlogListView,PostCreateView,PostDetailView

urlpatterns = [
    path('',PostListView.as_view(),name='index'),
    path('blogs',BlogListView.as_view(),name='blogs'),
    path('new_post',PostCreateView.as_view(),name='new_post'),
    path('<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('accounts/login/',UserLogin.as_view(),name='login'),
    path('accounts/logout/',UserLogout.as_view(),name='logout'),
]
