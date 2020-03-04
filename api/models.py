from django.db import models
from users.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(
        CustomUser, blank=True, related_name='student', limit_choices_to={'is_student': True})
    teachers = models.ManyToManyField(
        CustomUser, blank=True, related_name='teacher', limit_choices_to={'is_teacher': True})

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.course})'


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.lecture})'


class Homework(models.Model):
    solution_file = models.FileField(
        upload_to='uploads/solutions/')
    MARK_CHOICES = ((1, "1"), (2, "2"), (3, "2"),
                    (4, "4"), (5, "5"))
    mark = models.PositiveSmallIntegerField(
        blank=True, choices=MARK_CHOICES, default=1)
    student = models.ForeignKey(
        CustomUser,
        limit_choices_to={'is_student': True},
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)





