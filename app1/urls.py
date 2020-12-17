from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.demo_ajax,name='demo_ajax'),
    path('Save_DB',views.Save_DB,name='Save_DB'),
    path('validate',views.validate,name='validate'),
]
