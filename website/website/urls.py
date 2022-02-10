"""website URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView
import os

from . import views
favicon_view = RedirectView.as_view(url='/favicon.ico', permanent=True)
urlpatterns = [
    re_path(os.path.realpath(os.path.dirname(__file__)) + '/favicon.ico', favicon_view),
    path('', views.Athome, name='home'),
    path('home', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('pressite', views.pressite, name='pressite'),
    path('presperso', views.presperso, name='presperso'),
    path('projets', views.projets, name='projets'),
    path('rss', views.rss, name='rss'),
    path('afaire', views.afaire, name='afaire'),
    path('ml', views.ml, name='ml'),
    path("About",views.About,name="About"),
    path("Contact",views.Contact,name="Contact"),
    path("Mes-projets",views.Mesprojets,name="Mes-projets"),
    path("Le-site",views.Lesite,name="Le-site"),
    path("Mentions-légales",views.betaml,name="Mentions-légales"),
        path("Athome", views.Athome,name="Accueil")

]
