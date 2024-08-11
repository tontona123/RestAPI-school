# exam_app/admin.py
from django.urls import path
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from apis.models import Classroom, School, Student, Teacher


class MyAdminSite(admin.AdminSite):
    site_header = 'My Administration'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('summary/', self.admin_view(self.summary_view), name='summary'),
        ]
        return custom_urls + urls

    def has_permission(self, request):
        # ตรวจสอบให้แน่ใจว่าฟังก์ชันนี้คืนค่า True สำหรับ admin users
        return request.user.is_active and request.user.is_staff
    
    def summary_view(self, request):
        schools = School.objects.all()
        classrooms = Classroom.objects.all()
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        
        template = loader.get_template('admin/summary.html')
        context = {
            'schools': schools,
            'classrooms': classrooms,
            'students': students,
            'teachers': teachers,
        }
        return HttpResponse(template.render(context, request))

admin_site = MyAdminSite(name='myadmin')
