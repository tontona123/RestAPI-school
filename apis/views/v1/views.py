# apis/views/v1/views.py
from django.shortcuts import render
from apis.models import Classroom, School, Student, Teacher  # import โมเดล

def summary_view(request):
    schools = School.objects.all()
    classrooms = Classroom.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    context = {
        'schools': schools,
        'classrooms': classrooms,
        'students': students,
        'teachers': teachers,
    }

    return render(request, 'apis/summary.html', context)
