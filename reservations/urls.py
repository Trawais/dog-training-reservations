from django.urls import path
from . import views

app_name = 'reservations'
urlpatterns = [
    path('', views.courses, name='all'),
    path('course-calendar/<int:pk>/', views.course_detail_calendar, name='course-calendar'),
    path('course/<int:pk>/', views.course_detail, name='course'),
    path('course/lesson/<int:pk>/', views.lesson_detail, name='lesson'),
]
