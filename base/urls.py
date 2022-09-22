from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('publishers', views.publishers, name='publishers'),
    path('advertisers', views.advertisers, name='advertisers')

]
