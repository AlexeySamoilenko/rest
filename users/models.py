from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    STUDENT = 'Student'
    TEACHER = 'Teacher'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    role = models.CharField(choices=ROLE_CHOICES, null=True, blank=True, max_length=10, help_text='Role')
    enroll_number = models.PositiveIntegerField(null=True, unique=True, help_text='Enroll Number')

    def __str__(self):
        return self.user.username


class Lecture(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True)


class TeacherLecture(models.Model):
    TeacherID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    LectureID = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}_{}".format(self.TeacherID, self.LectureID)


class StudentLecture(models.Model):
    StudentID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    TeacherLectureID = models.ForeignKey(TeacherLecture, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)

    def __str__(self):
        return "{}_{}".format(self.StudentID, self.TeacherLectureID)