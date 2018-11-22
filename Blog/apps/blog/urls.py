from django.conf.urls import url
from . import views

urlpatterns = [
    url('post_list/', views.post_list, name='post_list'),
]