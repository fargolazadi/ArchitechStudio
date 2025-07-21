from django.urls import path
from blog.views import * 

app_name = 'blog'

urlpatterns = [
    path('',blog_index,name='blog'),
    path('persian/',blog_persian_index,name='blog-persian'),
    path('detail/<int:pid>/',blog_detail,name='blog-detail'),
    path('persian-detail/<int:pid>/',blog_persian_detail,name='blog-persian-detail'),
]