from django.contrib import admin
from .models import *

class LessonTabular(admin.TabularInline):
    model = Lesson
    extra = 2
    
class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'when_datetime', 'place', 'trainer']
    list_filter = ['course']
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonTabular]
    list_display = ['name', 'description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Participant)
