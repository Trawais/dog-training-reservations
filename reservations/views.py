from django.shortcuts import render, get_object_or_404
from calendar import Calendar
from .utils.calendar import prepare_lessons_dict

from .models import Course, Lesson

def courses(request):
    courses = Course.objects.all()
    return render(request, 'reservations/courses.html', { 'courses': courses} )

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if len(course.lesson_set.all()) == 0:
        return render(request, 'reservations/course_detail.html', { 'course': course, 'lessons': [] })

    min_date = min(course.lesson_set.all(), key=lambda x: x.when_datetime)
    max_date = max(course.lesson_set.all(), key=lambda x: x.when_datetime)
    
    lessons = prepare_lessons_dict(min_date.when_datetime, max_date.when_datetime)
        
    for lesson in course.lesson_set.all():
        for week in lessons[(lesson.when_datetime.year, lesson.when_datetime.month)]:
            if lesson.when_datetime.day in week:
                week[lesson.when_datetime.day].append(lesson)
                break
                

    return render(request, 'reservations/course_detail.html', { 'course': course, 'lessons': lessons })

def lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'reservations/lesson_detail.html', { 'lesson': lesson} )