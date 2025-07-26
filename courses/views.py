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
        return Course.objects.annotate(
            total_students=Count('enrollment', distinct=True),
            passed_students=Count('enrollment', filter=Q(enrollment__passed=True), distinct=True)
        )