"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
  
from django.contrib import admin # type: ignore
from django.urls import include,path # type: ignore
from .views import HomeView # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # type: ignore
from django.conf import settings # type: ignore
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name= 'index'),
    path("modulo1/", include('apps.modulo1.urls')),
    path("libros/", include('apps.libros.urls')),
    path("users/", include('apps.blog_auth.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 