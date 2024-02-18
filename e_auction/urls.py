"""
URL configuration for e_auction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from e_auctionapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("browseauction/", views.browseauction, name="browseauction"),
    path("mybid/", views.mybid, name="mybid"),
    path("myproduct/", views.myproduct, name="myproduct"),
    path("createauction/", views.createauction, name="createauction"),
    path("login", views.loginuser, name="login"),
    path("register", views.register, name="register"),
    path("userlogout", views.userlogout, name="userlogout"),
    path("contact", views.contact, name="contact"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("searchproduct", views.searchproduct, name="searchproduct"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)