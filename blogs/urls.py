from django.urls import path,include

from .views import PostListView,UserLogin,UserLogout,BlogListView

urlpatterns = [
    path('',PostListView.as_view(),name='index'),
    path('blogs',BlogListView.as_view(),name='blogs'),
    path('accounts/login/',UserLogin.as_view(),name='login'),
    path('accounts/logout/',UserLogout.as_view(),name='logout'),
]
