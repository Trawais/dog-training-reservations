from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
]
