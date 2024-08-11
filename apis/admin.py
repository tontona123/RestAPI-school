from django.urls import path
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from .models import Classroom, School, Student, Teacher
# สร้าง Base Admin Class ที่รวม Media class ไว้ในนี้
class BaseAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('apis/css/custom_admin.css',)  # ลิงก์ไปยัง custom CSS
        }
        js = ('apis/js/custom_admin.js',)  # ลิงก์ไปยัง custom JavaScript


@admin.register(Classroom)
class ClassroomAdmin(BaseAdmin):  # สืบทอดจาก BaseAdmin
    list_display = ('year', 'section', 'school')
    list_filter = ('school',)
    search_fields = ('year', 'section', 'school__name')
    ordering = ['school__name', 'year', 'section'] 


@admin.register(School)
class SchoolAdmin(BaseAdmin):  # สืบทอดจาก BaseAdmin
    list_display = ('name', 'abbreviation', 'address')
    search_fields = ('name', 'abbreviation', 'address')
    ordering = ('name',)


@admin.register(Teacher)
class TeacherAdmin(BaseAdmin):  
    list_display = ('firstname', 'lastname', 'gender')
    list_filter = ('classrooms',)
    search_fields = ('firstname', 'lastname')
    ordering = ('lastname', 'firstname')
    fieldsets = (
        (None, {
            'fields': ('firstname', 'lastname')
        }),
        ('Additional Info', {
            'fields': ('gender', 'classrooms')
        }),
    )


@admin.register(Student)
class StudentAdmin(BaseAdmin):  # สืบทอดจาก BaseAdmin
    list_display = ('firstname', 'lastname', 'gender', 'classroom')
    list_filter = ('classroom',)
    search_fields = ('firstname', 'lastname', 'classroom__section')
    ordering = ('lastname', 'firstname')
    actions = ['promote_students']

    def promote_students(self, request, queryset):
        # Logic to promote students
        new_classroom = None  # กำหนดค่า classroom ที่ต้องการให้ update
        rows_updated = queryset.update(classroom=new_classroom)  # เปลี่ยน classroom ของนักเรียน
        self.message_user(request, f'{rows_updated} students successfully promoted.')
    promote_students.short_description = 'Promote selected students'



