from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from students import views


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),


    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),


    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),


    path(
        '',
        views.home,
        name='home'
    ),


    path(
        'add-student/',
        views.add_student,
        name='add_student'
    ),

    path(
    'edit-student/<int:id>/',
    views.edit_student,
    name='edit_student'
    ),
    path(
    'delete-student/<int:id>/',
    views.delete_student,
    name='delete_student'
    ),
    path(
    'report-card/<int:id>/',
    views.generate_report_card,
    name='generate_report_card'
    ),
    path(
    'attendance/',
    views.add_attendance,
    name='add_attendance'
    ),

    path(
        'student/<int:id>/',
        views.student_detail,
        name='student_detail'
    ),
    path(
    'id-card/<int:id>/',
    views.generate_id_card,
    name='generate_id_card'
    ),
    path(
    'verify/<int:id>/',
    views.verify_student,
    name='verify_student'
    ),
    path(
    'reports/',
    views.reports,
    name='reports'
   ),

    path(
    'attendance-report/',
    views.attendance_report,
    name='attendance_report'
    ),


    path(
    'result-report/',
    views.result_report,
    name='result_report'
    ),


    path(
    'fee-report/',
    views.fee_report,
    name='fee_report'
    ),


    path(
    'export-students/',
    views.export_students_excel,
    name='export_students_excel'
    ),
    path(
    'attendance-report/',
    views.attendance_report,
    name='attendance_report'
    ),


    path(
    'result-report/',
    views.result_report,
    name='result_report'
    ),


    path(
    'fee-report/',
    views.fee_report,
    name='fee_report'
    ),


    path(
    'export-excel/',
    views.export_excel,
    name='export_excel'
    ),

]


# Media files (student photos)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)