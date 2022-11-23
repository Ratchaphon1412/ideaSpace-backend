from django.contrib import admin
from django.urls import path
from .views import CreatePost, SavePostView, ViewPost

urlpatterns = [
    path('post/', CreatePost.as_view()),
    path('post/save/', SavePostView.as_v