from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    login_view, logout_view, register_view, profile_view
)

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    
     # Blog post routes
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
