from rest_framework import viewsets
from rest_framework.response import Response
from .models import Course, Enrollment
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        courses = Course.objects.all()

        passed_min = request.query_params.get('passed_students__gte')
        passed_max = request.query_params.get('passed_students__lte')

        result = []
        for course in courses:
            total_students = Enrollment.objects.filter(course=course).count()
            passed_students = Enrollment.objects.filter(course=course, passed=True).count()
            pass_percentage = round((passed_students / total_students) * 100, 2) if total_students > 0 else 0

            if passed_min and passed_students < int(passed_min):
                continue 
            if passed_max and passed_students > int(passed_max):
                continue

            result.append({
                'id': course.id,           "کلید اصلی مدل کورس"
                'title': course.title,
                'instructor': course.instructor.id,
                'total_students': total_students,
                'passed_students': passed_students,
                'pass_percentage': pass_percentage
            })

        return Response(result)
