"""projectApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from projectApp.core import views as core_views
from django.contrib.auth import views as a_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>', core_views.index, name='index'),
    path('', core_views.home, name='home'),
    path('home/', core_views.home, name='home'),
    path('login/', a_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',  a_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('create/', core_views.create, name='create'),
    # path('dashboard/', core_views.d, name = 'dashboard'),
]
