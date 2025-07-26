from django.core.cache import cache
from django.db.models import Count, Q
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer
from .filters import CourseFilter


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter

    def get_queryset(self):
        queryset = cache.get('courses_list')
        if queryset is None:
            queryset = Course.objects.annotate(
                total_students=Count('enrollments', distinct=True),
                passed_students=Count('enrollments', filter=Q(enrollments__passed=True), distinct=True)
            )
            cache.set('courses_list', queryset, 300)
        return queryset