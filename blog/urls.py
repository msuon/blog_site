from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('posts', views.blog_list_view, name='post_list'),
    path('posts/page$', views.blog_page_view, name='post_page'),
    path('resume', views.resume_view, name='resume_page'),
]