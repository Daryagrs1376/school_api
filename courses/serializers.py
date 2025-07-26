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
    
#     اگر هیچ دانشجویی تو دوره ثبت‌نام نکرده بود (total == 0) ⇒ درصد قبولی رو 0 برمی‌گردونه (برای جلوگیری از تقسیم بر صفر).

# در غیر این صورت:

# تعداد قبولی‌ها تقسیم بر کل دانشجوها × 100 می‌کنه.

# با round(..., 2) هم عدد رو تا دو رقم اعشار گرد می‌کنه.