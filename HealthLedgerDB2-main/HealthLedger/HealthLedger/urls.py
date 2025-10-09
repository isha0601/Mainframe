"""
URL configuration for HealthLedger project.

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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CREATE, name='index'),
    path('new_record/', views.CREATE, name='home'),
    path('update_record/', views.UPDATE, name='update'),
    
    
    # APIS
    path('api/get_data_by_uid', views.get_data_by_uid, name='get_data_by_uid'),
    path('api/update_payment/', views.update_payment, name='update_payment'),
    path('api/load_data/', views.load_data, name='load_data'),

    # Employee pages
    path('employee/new_record/', views.EMP_CREATE, name='emp_create'),
    path('employee/update_record/', views.EMP_UPDATE, name='emp_update'),

    # Employee APIs
    path('api/employee/get_data_by_eid', views.get_data_by_eid, name='get_data_by_eid'),
    path('api/employee/update_payment/', views.update_emp_payment, name='update_emp_payment'),
    path('api/employee/load_data/', views.load_emp_data, name='load_emp_data'),
]
