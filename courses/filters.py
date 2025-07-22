import django_filters
from .models import Course, Enrollment



class CourseFilter(django_filters.FilterSet):
    passed_students__gte = django_filters.NumberFilter(method='filter_passed_students_gte')
    passed_students__lte = django_filters.NumberFilter(method='filter_passed_students_lte')


    class Meta:
        model = Course
        fields = []

    def filter_passed_students_gte(self, queryset, name, value):
        course_ids = [course.id for course in queryset if Enrollment.objects.filter(course=course, passed=True).count() >= value]
        return queryset.filter(id__in=course_ids)


    def filter_passed_students_lte(self, queryset, name, value):
        course_ids = [course.id for course in queryset if Enrollment.objects.filter(course=course, passed=True).count() <= value]
        return queryset.filter(id__in=course_ids)