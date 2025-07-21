from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.FloatField(null=True, blank=True)
    passed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.student} in {self.course}"
