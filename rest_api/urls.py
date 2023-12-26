from django.urls import path

from rest_api import views

urlpatterns = [
    path('', views.emp_list, name="view"),
    path('view1/<int:pk>/',views.emp_details, name="view1"),
]