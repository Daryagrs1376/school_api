from rest_framework import serializers
from .models import Course, Enrollment



class CourseSerializer(serializers.ModelSerializer):
    total_students = serializers.SerializerMethodField()
    passed_students = serializers.SerializerMethodField()
    pass_percentage = serializers.SerializerMethodField()


    class Meta:
        model = Course
        fields = ['id', 'title', 'instructor', 'total_students', 'passed_students', 'pass_percentage']


    def get_total_students(self, obj):
        return Enrollment.objects.filter(course=obj).count()


    def get_passed_students(self, obj):
        return Enrollment.objects.filter(course=obj, passed=True).count()


    # def get_pass_percentage(self, obj):
    #     total = self.get_total_students(obj)
    #     passed = self.get_passed_students(obj)
    #     if total == 0:
    #         return 0
    #     return round((passed / total) * 100, 2)
