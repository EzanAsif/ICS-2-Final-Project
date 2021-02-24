from django.urls import path, re_path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list, name="list"),
    path('create/', views.review_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.review_detail, name="detail"),
]
 
