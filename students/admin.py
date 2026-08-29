from django.contrib import admin
from .models import Student, ClassRoom, Teacher, Fee, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'classroom', 'phone')


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'subject', 'teacher')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'month', 'amount', 'status')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks')