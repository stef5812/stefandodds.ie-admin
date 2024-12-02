from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/success/', views.gallery_success_view, name='gallery_success'),
]
