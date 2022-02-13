"""visa_consultant URL Configuration

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
from django.urls import path, include

# from client.views import index,about,contact,gallery,services,typography
from django.contrib.auth.views import LoginView,LogoutView
from django .conf import settings
from django .conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('client.urls')),
    path("", LoginView.as_view(template_name="client/login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="client/logout.html"), name="logout"),

    # path('index/',index,name="index"),
    # path("about/",about,name="about"),
    # path("contact/",contact,name="contact"),
    # path("gallery/",gallery,name="gallery"),
    # path("services/",services,name="services"),
]
