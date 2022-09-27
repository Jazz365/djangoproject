from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('publishers', views.publishers, name='publishers'),
    path('advertisers', views.advertisers, name='advertisers'),
    path('traffic', views.traffic, name='traffic'),
    path('company', views.company, name='company'),
    path('contact-us', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),


]
