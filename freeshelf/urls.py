"""freeshelf URL Configuration

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
from django.urls import path, include

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('category/<slug:cat>', views.cat_list, name='cat_list'),
    path('suggestion/', views.book_suggestion, name='book_suggestion'),
    # path('login/', views.log_in, name='log_in'  ),
    path('accounts/', include('registration.backends.default.urls')),
    path('suggestions/', views.suggestion_list, name='suggestion_list'),
    path('favorite/<int:pk>', views.favorite, name='favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),

]
