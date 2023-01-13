from django.urls import path
from . import views

app_name = 'reservations'
urlpatterns = [
    path('courses/', views.courses, name='all'),
    path('course/<int:pk>/', views.course_detail, name='course'),
    path('course/lesson/<int:pk>/', views.lesson_detail, name='lesson'),
]
