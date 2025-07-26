from django.contrib import admin
from .models import Course, Enrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor')
    search_fields = ('title', 'instructor__username')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'student', 'grade', 'passed')
    list_filter = ('passed', 'course')
    search_fields = ('student__username', 'course__title')