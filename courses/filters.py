import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    passed_students__gte = django_filters.NumberFilter(field_name='passed_students', lookup_expr='gte')
    passed_students__lte = django_filters.NumberFilter(field_name='passed_students', lookup_expr='lte')
    total_students__gte = django_filters.NumberFilter(field_name='total_students', lookup_expr='gte')

    class Meta:
        model = Course
        fields = ['passed_students__gte', 'passed_students__lte', 'total_students__gte']
