from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse
from datetime import date
from reportlab.lib import colors
import qrcode
from io import BytesIO
from reportlab.lib.utils import ImageReader
from django.db.models import Avg, Sum
from openpyxl import Workbook
from datetime import datetime
from .models import (
    Student,
    Result,
    Fee,
    Teacher,
    ClassRoom,
    Attendance
)

from .forms import (
    StudentForm,
    ResultForm,
    FeeForm,
    AttendanceForm
)



# =========================
# DASHBOARD
# =========================

@login_required
def home(request):

    try:
        teacher = Teacher.objects.get(
            user=request.user
        )

        classrooms = ClassRoom.objects.filter(
            teacher=teacher
        )

        students = Student.objects.filter(
            classroom__in=classrooms
        )

    except Teacher.DoesNotExist:

        students = Student.objects.all()
        classrooms = ClassRoom.objects.all()



    search = request.GET.get("search")

    if search:
        students = students.filter(
            name__icontains=search
        )



    results = Result.objects.filter(
        student__in=students
    )


    fees = Fee.objects.filter(
        student__in=students,
        status="Paid"
    )



    attendance_records = Attendance.objects.filter(
        student__in=students
    )


    total_attendance = attendance_records.count()

    present_attendance = attendance_records.filter(
        status="Present"
    ).count()



    if total_attendance:

        attendance_percentage = round(
            (present_attendance / total_attendance) * 100
        )

    else:

        attendance_percentage = 0



    context = {

        "students":students,

        "total_students":students.count(),

        "classrooms":classrooms.count(),

        "total_results":results.count(),

        "fees_collected":sum(
            fee.amount for fee in fees
        ),

        "attendance_percentage":attendance_percentage,

    }


    return render(
        request,
        "home.html",
        context
    )



# =========================
# ADD STUDENT
# =========================

@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            form.save()

            return redirect("home")


    else:

        form = StudentForm()



    return render(
        request,
        "add_student.html",
        {
            "form":form
        }
    )
# =========================
# STUDENT DETAIL
# =========================

@login_required
def student_detail(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )


    results = Result.objects.filter(
        student=student
    )


    fees = Fee.objects.filter(
        student=student
    )


    attendance = Attendance.objects.filter(
        student=student
    )


    total_days = attendance.count()


    present_days = attendance.filter(
        status="Present"
    ).count()



    if total_days:

        attendance_percentage = round(
            (present_days / total_days) * 100
        )

    else:

        attendance_percentage = 0



    return render(
        request,
        "student_detail.html",
        {
            "student":student,
            "results":results,
            "fees":fees,
            "attendance":attendance,
            "attendance_percentage":attendance_percentage,
        }
    )



# =========================
# EDIT STUDENT
# =========================


@login_required
def edit_student(request,id):

    student = get_object_or_404(
        Student,
        id=id
    )


    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )


        if form.is_valid():

            form.save()


            return redirect(
                "student_detail",
                id=student.id
            )


    else:

        form = StudentForm(
            instance=student
        )


    return render(
        request,
        "edit_student.html",
        {
            "form":form,
            "student":student
        }
    )



# =========================
# DELETE STUDENT
# =========================


@login_required
def delete_student(request,id):

    student = get_object_or_404(
        Student,
        id=id
    )


    if request.method == "POST":

        student.delete()

        return redirect("home")



    return render(
        request,
        "delete_student.html",
        {
            "student":student
        }
    )



# =========================
# RESULTS
# =========================


@login_required
def add_result(request):

    if request.method=="POST":

        form = ResultForm(
            request.POST
        )


        if form.is_valid():

            form.save()

            return redirect("home")


    else:

        form = ResultForm()



    return render(
        request,
        "add_result.html",
        {
            "form":form
        }
    )



@login_required
def edit_result(request,id):

    result = get_object_or_404(
        Result,
        id=id
    )


    if request.method=="POST":

        form = ResultForm(
            request.POST,
            instance=result
        )


        if form.is_valid():

            form.save()

            return redirect(
                "student_detail",
                id=result.student.id
            )


    else:

        form = ResultForm(
            instance=result
        )


    return render(
        request,
        "edit_result.html",
        {
            "form":form
        }
    )



@login_required
def delete_result(request,id):

    result = get_object_or_404(
        Result,
        id=id
    )


    student_id=result.student.id


    if request.method=="POST":

        result.delete()

        return redirect(
            "student_detail",
            id=student_id
        )


    return render(
        request,
        "delete_result.html",
        {
            "result":result
        }
    )



# =========================
# FEES
# =========================


@login_required
def add_fee(request):

    if request.method=="POST":

        form = FeeForm(
            request.POST
        )


        if form.is_valid():

            form.save()

            return redirect("home")


    else:

        form=FeeForm()



    return render(
        request,
        "add_fee.html",
        {
            "form":form
        }
    )



@login_required
def edit_fee(request,id):

    fee=get_object_or_404(
        Fee,
        id=id
    )


    if request.method=="POST":

        form=FeeForm(
            request.POST,
            instance=fee
        )


        if form.is_valid():

            form.save()

            return redirect(
                "student_detail",
                id=fee.student.id
            )


    else:

        form=FeeForm(
            instance=fee
        )


    return render(
        request,
        "edit_fee.html",
        {
            "form":form
        }
    )



@login_required
def delete_fee(request,id):

    fee=get_object_or_404(
        Fee,
        id=id
    )


    student_id=fee.student.id


    if request.method=="POST":

        fee.delete()

        return redirect(
            "student_detail",
            id=student_id
        )


    return render(
        request,
        "delete_fee.html",
        {
            "fee":fee
        }
    )
# =========================
# ATTENDANCE
# =========================


@login_required
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(
            request.POST
        )


        if form.is_valid():

            form.save()

            return redirect(
                "home"
            )


    else:

        form = AttendanceForm()



    return render(
        request,
        "add_attendance.html",
        {
            "form":form
        }
    )



# =========================
# GENERATE REPORT CARD PDF
# =========================


@login_required
def generate_report_card(request,id):

    student = get_object_or_404(
        Student,
        id=id
    )


    results = Result.objects.filter(
        student=student
    )


    fees = Fee.objects.filter(
        student=student
    )


    attendance = Attendance.objects.filter(
        student=student
    )



    response = HttpResponse(
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        f'attachment; filename="{student.name}_report_card.pdf"'
    )



    pdf = canvas.Canvas(
        response,
        pagesize=letter
    )


    width,height = letter



    # Title

    pdf.setFont(
        "Helvetica-Bold",
        20
    )


    pdf.drawCentredString(
        width/2,
        height-50,
        "Student Report Card"
    )



    pdf.setFont(
        "Helvetica",
        12
    )



    y = height-100



    # Student Information


    pdf.drawString(
        50,
        y,
        f"Name: {student.name}"
    )


    y -=25


    pdf.drawString(
        50,
        y,
        f"Roll Number: {student.roll_number}"
    )


    y -=25


    pdf.drawString(
        50,
        y,
        f"Class: {student.classroom}"
    )



    y -=40



    # Results


    pdf.setFont(
        "Helvetica-Bold",
        14
    )


    pdf.drawString(
        50,
        y,
        "Results"
    )


    y -=25



    pdf.setFont(
        "Helvetica",
        12
    )



    total_marks = 0
    subjects = 0



    for result in results:


        pdf.drawString(
            60,
            y,
            f"{result.subject}: {result.marks}"
        )


        total_marks += result.marks

        subjects += 1


        y -=20




    if subjects > 0:

        percentage = (
            total_marks / (subjects * 100)
        ) * 100

    else:

        percentage = 0




    y -=20



    pdf.drawString(
        50,
        y,
        f"Percentage: {percentage:.2f}%"
    )


    y -=25



    if percentage >= 80:

        grade="A"


    elif percentage >=60:

        grade="B"


    elif percentage >=40:

        grade="C"


    else:

        grade="F"



    pdf.drawString(
        50,
        y,
        f"Grade: {grade}"
    )



    y -=40



    # Attendance


    pdf.drawString(
        50,
        y,
        f"Attendance Days: {attendance.count()}"
    )



    y -=30



    # Fees


    paid = fees.filter(
        status="Paid"
    ).count()



    pdf.drawString(
        50,
        y,
        f"Paid Fees: {paid}"
    )



    # Student Photo (if exists)

    if student.photo:

        try:

            from reportlab.lib.utils import ImageReader


            pdf.drawImage(
                ImageReader(student.photo.path),
                width-150,
                height-150,
                width=80,
                height=80
            )


        except:

            pass



    pdf.save()


    return response
# =========================
# GENERATE STUDENT ID CARD
# =========================

@login_required
def generate_id_card(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )


    response = HttpResponse(
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        f'attachment; filename="{student.name}_ID_Card.pdf"'
    )


    pdf = canvas.Canvas(
        response,
        pagesize=letter
    )


    width, height = letter


    # Card position

    x = 100
    y = height - 400

    card_width = 400
    card_height = 250



    # Outer card

    pdf.setStrokeColor(
        colors.darkblue
    )

    pdf.setLineWidth(
        3
    )

    pdf.roundRect(
        x,
        y,
        card_width,
        card_height,
        15
    )



    # Header

    pdf.setFillColor(
        colors.darkblue
    )

    pdf.rect(
        x,
        y + 200,
        card_width,
        50,
        fill=1
    )


    pdf.setFillColor(
        colors.white
    )


    pdf.setFont(
        "Helvetica-Bold",
        18
    )


    pdf.drawCentredString(
        width/2,
        y+220,
        "ABC SCHOOL MANAGEMENT SYSTEM"
    )


    pdf.setFont(
        "Helvetica",
        12
    )


    pdf.drawCentredString(
        width/2,
        y+205,
        "STUDENT ID CARD"
    )



    # Photo

    if student.photo:

        try:

            pdf.drawImage(
                ImageReader(student.photo.path),
                x+25,
                y+70,
                width=90,
                height=100
            )


        except:

            pass



    # Details

    pdf.setFillColor(
        colors.black
    )


    pdf.setFont(
        "Helvetica-Bold",
        12
    )


    details_x = x+140



    pdf.drawString(
        details_x,
        y+150,
        f"Name: {student.name}"
    )


    pdf.drawString(
        details_x,
        y+125,
        f"Roll No: {student.roll_number}"
    )


    pdf.drawString(
        details_x,
        y+100,
        f"Class: {student.classroom}"
    )


    pdf.drawString(
        details_x,
        y+75,
        f"Student ID: {student.id}"
    )



    # Issue date

    pdf.setFont(
        "Helvetica",
        10
    )


    pdf.drawString(
        x+25,
        y+35,
        f"Issue Date: {date.today()}"
    )



    # Signature

    pdf.line(
        x+280,
        y+40,
        x+360,
        y+40
    )


    pdf.drawString(
        x+295,
        y+25,
        "Principal"
    )



    # QR Code

    qr_data = (
        f"Name: {student.name}\n"
        f"Roll: {student.roll_number}\n"
        f"ID: {student.id}"
    )


    qr = qrcode.make(
        qr_data
    )


    qr_buffer = BytesIO()

    qr.save(
        qr_buffer,
        format="PNG"
    )


    qr_buffer.seek(0)



    pdf.drawImage(
        ImageReader(qr_buffer),
        x+300,
        y+70,
        width=60,
        height=60
    )



    pdf.save()


    return response
def verify_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    return render(
        request,
        "verify_student.html",
        {
            "student":student
        }
    )
# ==========================
# REPORTS DASHBOARD
# ==========================

@login_required
def reports(request):

    total_students = Student.objects.count()


    total_fees = Fee.objects.filter(
        status="Paid"
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0



    attendance = Attendance.objects.all()


    total_attendance = attendance.count()


    present = attendance.filter(
        status="Present"
    ).count()



    if total_attendance:

        attendance_percentage = round(
            (present / total_attendance) * 100
        )

    else:

        attendance_percentage = 0



    average_result = Result.objects.aggregate(
        avg=Avg("marks")
    )["avg"] or 0



    return render(
        request,
        "reports.html",
        {
            "total_students":total_students,
            "total_fees":total_fees,
            "attendance_percentage":attendance_percentage,
            "average_result":round(average_result,2)
        }
    )



# ==========================
# ATTENDANCE REPORT
# ==========================

@login_required
def attendance_report(request):

    records = Attendance.objects.all()


    return render(
        request,
        "attendance_report.html",
        {
            "records":records
        }
    )



# ==========================
# RESULT REPORT
# ==========================

@login_required
def result_report(request):

    results = Result.objects.all()


    return render(
        request,
        "result_report.html",
        {
            "results":results
        }
    )



# ==========================
# FEE REPORT
# ==========================

@login_required
def fee_report(request):

    fees = Fee.objects.all()


    return render(
        request,
        "fee_report.html",
        {
            "fees":fees
        }
    )



# ==========================
# EXPORT REPORT EXCEL
# ==========================


@login_required
def export_students_excel(request):

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Students"



    sheet.append(
        [
            "Name",
            "Roll Number",
            "Class",
            "Phone"
        ]
    )


    students = Student.objects.all()


    for student in students:

        sheet.append(
            [
                student.name,
                student.roll_number,
                str(student.classroom),
                student.phone
            ]
        )



    response = HttpResponse(
        content_type=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    response["Content-Disposition"] = (
        "attachment; filename=students.xlsx"
    )


    workbook.save(response)


    return response
from django.db.models import Sum
from openpyxl import Workbook
from django.http import HttpResponse


@login_required
def attendance_report(request):

    students = Student.objects.all()

    attendance_data = []

    for student in students:

        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status="Present"
        ).count()


        if total > 0:
            percentage = round((present/total)*100)
        else:
            percentage = 0


        attendance_data.append({
            "student":student,
            "total":total,
            "present":present,
            "percentage":percentage
        })


    return render(
        request,
        "attendance_report.html",
        {
            "attendance_data":attendance_data
        }
    )




@login_required
def result_report(request):

    results = Result.objects.all()


    return render(
        request,
        "result_report.html",
        {
            "results":results
        }
    )





@login_required
def fee_report(request):

    fees = Fee.objects.all()


    total_paid = Fee.objects.filter(
        status="Paid"
    ).aggregate(
        total=Sum("amount")
    )


    return render(
        request,
        "fee_report.html",
        {
            "fees":fees,
            "total_paid":total_paid["total"] or 0
        }
    )






@login_required
def export_excel(request):

    students = Student.objects.all()


    workbook = Workbook()

    sheet = workbook.active

    sheet.title="Students"



    sheet.append([
        "Name",
        "Roll Number",
        "Class",
        "Phone"
    ])



    for student in students:

        sheet.append([
            student.name,
            student.roll_number,
            str(student.classroom),
            student.phone
        ])



    response = HttpResponse(
        content_type=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    response["Content-Disposition"] = (
        'attachment; filename="students.xlsx"'
    )


    workbook.save(response)


    return response