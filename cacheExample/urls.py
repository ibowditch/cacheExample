"""
URL configuration for cacheExample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from premier import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', views.GamesList.as_view(), name='games'),
    path('games2/', views.GamesTableView.as_view(), name='games2'),
    path('games2t/<str:team>', views.GamesTableView.as_view(), name='games2t'),
]
