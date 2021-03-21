"""budgetcoach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings  #this is for displaying image
from django.conf.urls.static import static #this is for displaying image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminauth/', include('adminauth.urls')),
    path('admindashboard/', include('admindashboard.urls')),
    path('adminusers/', include('adminusers.urls')),
    path('adminbudgetcategories/', include('adminbudgetcategories.urls')),
    path('admintaxcategory/', include('admintaxcategory.urls')),
    path('adminsavingcategory/', include('adminsavingcategory.urls')),
    #user apps
    path('', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('userdetails/', include('userdetails.urls')),
    path('monthlyexpenses/', include('monthlyexpenses.urls')),
    path('actualexpenses/', include('actualexpenses.urls')),
    #for subadmin
    path('subadminauth/', include('subadminauth.urls')),
    path('subadmindashboard/', include('subadmindashboard.urls')),
    path('subadminusers/', include('subadminusers.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


9

