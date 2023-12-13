from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='studentlist'),
    path('create/', views.createStudent, name='createstudent'),
]
