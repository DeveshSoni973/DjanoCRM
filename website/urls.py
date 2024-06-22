from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('logout/',  views.logout_user, name='logout'),
path('register/',  views.register_user, name='register'),
path('record/<int:pk>', views.customer_record, name="record"),
path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
path('add_record/', views.add_record, name="add_record"),
path('update_record/<int:pk>/', views.update_record, name='update_record'),
]
'''In a Django project, the urls.py file is essential for routing URLs to the appropriate views. 
It acts as a map for the application, directing incoming web requests to the 
correct view based on the URL pattern. '''