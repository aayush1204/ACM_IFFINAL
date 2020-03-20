from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('',views.if_home,name='if_home'),
    path('job-listings/',views.job_list, name= 'job-listings'),
    path('job-single/<str:value>', views.job_single, name= 'job-single'),
    path('job-listings/job-single/<str:value>', views.job_single, name= 'job-single')
    
]
