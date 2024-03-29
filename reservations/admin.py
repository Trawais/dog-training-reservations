from django.contrib import admin
from .models import *

class LessonTabular(admin.TabularInline):
    model = Lesson
    fields = ['trainer', 'place', 'when_datetime', 'capacity', 'description']
    show_change_link = True

class ParticipantTabular(admin.TabularInline):
    model = Participant
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonTabular]
    list_display = ['name', 'description', 'password']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'pk', 'when_datetime', 'place', 'trainer']
    list_filter = ['course']
    inlines = [ParticipantTabular]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
