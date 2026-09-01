# Student Management System

A complete Django-based Student Management System designed to manage students, attendance, results, fees, profiles, ID cards, QR verification, and reporting.

## Features

### Student Management

- Add new students
- Edit student information
- Delete student records
- View student profiles
- Upload student photos

### Attendance Management

- Mark student attendance
- Track attendance percentage
- View student attendance
- Generate attendance reports

### Result Management

- Add student results
- Calculate percentage
- Generate grades
- View student results
- Generate result reports

### Fee Management

- Record student fees
- Track paid and unpaid fees
- View student fee records
- Generate fee reports

### Student ID Card

- Generate student ID cards
- Include:
  - Student photo
  - Student name
  - Roll number
  - Class
  - School information

### PDF Reports

- Generate student report cards
- Generate PDF reports
- Export reports

### Excel Export

- Export student records to Excel
- Manage student data in spreadsheet format

### QR Code Verification

- Generate QR codes for student verification
- Verify student information using QR codes

### Responsive Design

- Mobile-friendly dashboard
- Modern navigation
- Professional user interface

---

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap
- JavaScript
- SQLite
- ReportLab
- QR Code Generation

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dasboard.png)

### Dashboard 2

![Dashboard 2](screenshots/dashboard%202.png)

### Admin Portal

![Admin Portal](screenshots/admin%20portal.png)

### Add Student

![Add Student](screenshots/add%20student.png)

### Student Profile

![Student Profile](screenshots/student%20profile%20.png)

### Student Report Card

![Student Report Card](screenshots/student%20reportcard.png)

### Student Attendance

![Student Attendance](screenshots/attendaance%20of%20student.png)

### Mark Attendance

![Mark Attendance](screenshots/mark%20attendence.png)

### Attendance Report

![Attendance Report](screenshots/attendence%20report.png)

### Result Report

![Result Report](screenshots/result%20report.png)

### Result and Fee of Student

![Result and Fee](screenshots/result%20fee%20of%20student.png)

### Fee Report

![Fee Report](screenshots/fee%20report.png)

### Student Excel Sheet

![Student Excel Sheet](screenshots/student%20excel%20sheet.png)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmberHafeez-eng/Student-Management-System.git
cd Student-Management-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create your admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## Project Structure

```text
Student-Management-System/
│
├── dashboard/
├── students/
├── school_system/
├── media/
├── screenshots/
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## Database

The project uses SQLite as the default database.

---

## Author

**Amber Hafeez**

GitHub: https://github.com/AmberHafeez-eng
