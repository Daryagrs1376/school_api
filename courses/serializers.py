from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    pass_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'instructor', 'total_students', 'passed_students', 'pass_percentage']

    def get_pass_percentage(self, obj):
        total = obj.total_students or 0
        passed = obj.passed_students or 0
        return 0 if total == 0 else round((passed / total) * 100, 2)
