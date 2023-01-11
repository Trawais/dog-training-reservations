from django.contrib import admin
from .models import *

class LessonTabular(admin.TabularInline):
    model = Lesson

class ParticipantTabular(admin.TabularInline):
    model = Participant

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonTabular]
    list_display = ['name', 'description']
class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'when_datetime', 'place', 'trainer']
    list_filter = ['course']
    inlines = [ParticipantTabular]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
