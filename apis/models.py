from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    year = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)

    class Meta:
        ordering = ['school__name', 'year', 'section']
    
    def __str__(self):
        return f"{self.school.name} - {self.year}/{self.section}"

class Teacher(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
