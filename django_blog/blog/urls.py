from django.urls import path
from .views import post_create,post_list,post_delete,post_update,sanatcilar,post_detail

urlpatterns = [
    path('', post_list, name='post-list'),
    path('post-create/', post_create,name='post-create'),
    path('post-detail/<slug:slug>/', post_detail, name='post-detail'),
    path('post-update/<slug:slug>/', post_update, name='post-update'),
    path('post-delete/<slug:slug>/', post_delete, name='post-delete'),
    path('sanatcilar/(<int:sayi>', sanatcilar)

   ]