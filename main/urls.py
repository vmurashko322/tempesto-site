"""tempesto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

# from .views import show_base, main_page, show_equipment, show_service, show_rent, show_certificates, success_view, your_select, show_simple, show_usual
from main.views import main_page, show_base, show_equipment, show_service, show_rent, show_certificates, success_view, \
    your_select, show_simple, show_usual

urlpatterns = [
    path('', main_page, name='main'),
    path('base/', show_base, name='show'),
    path('equipment/', show_equipment, name='equipment'),
    path('service/', show_service, name='service'),
    path('rent/', show_rent, name='rent'),
    path('certificates/', show_certificates, name='certificates'),
    path('success/', success_view, name='success'),
    path('select/', your_select, name='select'),
    path('simple/', show_simple, name='show_simple'),
    path('usual/', show_usual, name='show_usual'),
]
