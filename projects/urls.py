from projects.views import *
from django.urls import path

app_name='projects'

urlpatterns=[
    path('',projects_index,name='all'),
    path('<int:pid>/',one_item,name='item'),
    path('category/<str:cat_name>/',categories,name='cat'),
    path('status/<str:sta_value>',statuses,name='stat'),
    path('sort/<str:sort_by>',sort_projects,name='sort'),
    path('persian/',projects_index_persian,name='all-persian'),
    path('persian/<int:pid>-persian/',one_item_persian,name='item-persian'),
    path('category-persian/<str:cat_name>/',categories_persian,name='cat-persian'),
    path('status-persian/<str:sta_value>',statuses_persian,name='stat-persian'),
    path('sort-persian/<str:sort_by>',sort_projects_persian,name='sort-persian'),
]