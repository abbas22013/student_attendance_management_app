from django.db import models



class Class(models.Model):
    instructor_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    class_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_code} - {self.instructor_name}"

class Student(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    major = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
