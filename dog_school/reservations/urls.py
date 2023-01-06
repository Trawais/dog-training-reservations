from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('courses/', views.courses, name='all'),
    path('course/<int:pk>/', views.course_detail, name='detail'),
]
