# """
# URL configuration for HealthLedger project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from . import views
# from django.http import HttpResponse
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", views.DASH, name="Dashboard"),
    
#     # APIS
#     path("api/get_stats/", views.get_stats, name="get_stats"),
#     path("api/matched/", views.get_matched, name="get_matched"),
#     path("api/recent-activity/", views.get_recent_activity, name="recent_activity"),
#      # Add new employee API
#     path("api/add_new_data/", views.add_new_data, name="add_new_data"),


#     # Add these endpoints
# path("api/get_employee/", views.get_employee, name="get_employee"),
# path("api/update_employee/", views.update_employee, name="update_employee"),



# path('employees/', views.view_all_employees, name='view_all_employees'),
#     path('api/delete_employee/', views.delete_employee, name='delete_employee'),
#     # You can also add create/update URLs
#     path('employees/update/<int:emp_id>/', views.update_employee, name='update_employee'),
#     path('employees/create/', views.create_employee, name='create_employee'),

# ]




from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard
    path('', views.DASH, name='dashboard'),

    # Employee Pages
    path('employees/', views.view_all_employees, name='view_all_employees'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/update/<str:emp_id>/', views.update_employee_page, name='update_employee_page'),

    # APIs
    path('api/get_stats/', views.get_stats, name='get_stats'),
    path('api/matched/', views.get_matched, name='get_matched'),
    path('api/recent-activity/', views.get_recent_activity, name='recent_activity'),
    path('api/add_new_data/', views.add_new_data, name='add_new_data'),
    path('api/get_employee/', views.get_employee, name='get_employee'),
    path('api/update_employee/', views.update_employee, name='update_employee'),
    path('api/delete_employee/', views.delete_employee, name='delete_employee'),
]
