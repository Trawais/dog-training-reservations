from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Course

def courses(request):
    courses = Course.objects.all()
    return render(request, 'reservations/courses.html', { 'courses': courses} )

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'reservations/course_detail.html', { 'course': course })
