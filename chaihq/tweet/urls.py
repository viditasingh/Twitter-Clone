from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.listTweets, name='tweet_list'),
    path('create',views.createTweet, name='create_tweet'),
    path('<int:tweet_id>/edit',views.editTweet, name='edit_tweet'),
    path('<int:tweet_id>/delete',views.deleteTweet, name='delete_tweet'),
    path('register/',views.register, name='register')
]