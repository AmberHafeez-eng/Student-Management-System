from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username


class ClassRoom(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.class_name} - {self.subject}"


class Student(models.Model):
    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(
    upload_to='student_photos/',
    blank=True,
    null=True
)
    def __str__(self):
        return self.name


class Fee(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    month = models.CharField(max_length=20)
    amount = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("Paid", "Paid"),
            ("Unpaid", "Unpaid")
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.month}"


class Result(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=100)

    marks = models.IntegerField()

    total_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"

    def grade(self):
        percentage = (self.marks / self.total_marks) * 100

        if percentage >= 80:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.student.name} - {self.subject}"
class Attendance(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=10,
        choices=[
            ("Present","Present"),
            ("Absent","Absent")
        ]
    )


    def __str__(self):

        return f"{self.student.name} - {self.status}"