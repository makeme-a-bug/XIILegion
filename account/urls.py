from django.contrib import admin
from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('',views.homepage,name='home'),
    path('createpost',views.createPost.as_view(),name='createpost'),
    path('deletepost/<int:pk>/delete',views.deletepost.as_view(),name='deletepost'),
    path('updatepost/<int:pk>/update',views.updatepost.as_view(),name='updatepost'),
    path('posts/<int:pk>/',  views.detailposts, name="detail"),
    path('posts/',  views.listview, name="list"),
    path('signup/',views.SignUp.as_view(),name="signup"),
    path('forums/',views.forumlist,name='forums'),
    path('forumsdetails/<int:pk>',views.forumdetail,name='forumdetail'),
    path('threaddetails/<int:pk>',views.threaddetail,name='threaddetail'),
    path('createThreadCategory/',views.createThreadCategory.as_view(),name='createThreadCategory'),
    path('deleteThreadCategory/<int:pk>/delete',views.deleteThreadCategory.as_view(),name='deleteThreadCategory'),
    path('updateThreadCategory/<int:pk>/update',views.updateThreadCategory.as_view(),name='updateThreadCategory'),
    path('addgame/',views.creategame.as_view(),name='creategame'),
    path('addThread/',views.createThread.as_view(),name='createThread'),
    path('deleteThread/<int:pk>/delete',views.deleteThread.as_view(),name='deleteThread'),
    path('updateThread/<int:pk>/update',views.updateThread.as_view(),name='updateThread'),
    path('games/',views.gamelist,name='games'),
    path('gamedetails/<int:pk>',views.gamedetail,name='gamedetail'),
    path('deletegame/<int:pk>/delete',views.deletegame.as_view(),name='deletegame'),
    path('updategame/<int:pk>/update',views.updategame.as_view(),name='updategame'),
    path('login/',views.login,name='login'),









]
