from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.basic_home),
    url(r'^all_tests/', views.all_tests),
    url(r'^my_tests/', views.my_tests),
    url(r'^new_test/', views.new_test, name='testform'),
    url(r'^get_names/', views.get_names, name='getnames'),
]
