#created in part2
from django.urls import path
from .views import (
                    PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )
from . import views #this imports something from current directory, that is views.py that we just made


urlpatterns = [
    #dont need any path, because this is for all blog sites
    #path('', views.home, name='blog-home'), #sends it to views.home where views is the thing we imported
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'), #handles blog/about
]


# <app>/<model>_<viewtype>.html
# 	blog/post_list.html
