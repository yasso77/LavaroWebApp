from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('send_email/', views.send_email, name='send_email'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.about, name='testimonials'),
    path('about/', views.about, name='about'),
]