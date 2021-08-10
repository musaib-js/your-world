from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import Services

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.handleLogin, name = "handleLogin"),
    path('signup', views.handleSignUp, name = "handleSignUp"),
    path('logout', views.handleLogout, name = "handleLogout"),
    path('about/', views.about, name = "about"),
    path('services/', views.services, name = "services"),
    path('contact/', views.contact, name = "contact"),
     path('<str:slug>/', views.service, name='service'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)