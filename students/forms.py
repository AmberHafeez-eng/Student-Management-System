from django import forms
from .models import Student, Result, Fee
from .models import Attendance

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            'name',
            'roll_number',
            'phone',
            'classroom',
            'photo'
        ]

class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = [
            "student",
            "status"
        ]

class ResultForm(forms.ModelForm):

    class Meta:
        model = Result

        fields = [
            "student",
            "subject",
            "marks",
            "total_marks",
        ]



class FeeForm(forms.ModelForm):

    class Meta:
        model = Fee

        fields = [
            "student",
            "month",
            "amount",
            "status",
        ]