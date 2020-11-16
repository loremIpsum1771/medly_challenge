"""medly_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from rest_countries.views import(
    CountriesView,
    CountryView,
    FlagView,
)

urlpatterns = [
    path('',CountriesView.as_view() ,name='countries'),
    path('all/',CountriesView.as_view() ,name='countries'),
    path('alpha/<str:code>/',CountryView.as_view() ,name='country'),
    path('alpha/<str:code>.svg',FlagView.as_view() ,name='flag'),
    path('admin/', admin.site.urls),
]
