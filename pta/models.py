from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classinfo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class ParentalUnit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_assigned = models.DateField(default=date.today)
    due_date = models.DateField(blank=True, null=True)
    points = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=1)

    def __str__(self):
        return self.teacher.user.username + ' ' + self.title

    class Meta:
        verbose_name_plural = 'Homework'
        ordering = ['-date_assigned']

class HomeworkGrade(models.Model):
    homework = models.ForeignKey(Homework, null=False, on_delete=models.CASCADE)
    parentalunit = models.ForeignKey(ParentalUnit, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.homework.__str__() + ' ' + self.parentalunit.__str__()


class WishlistItem(models.Model):
    description = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    parentalUnit = models.ForeignKey(ParentalUnit, blank=True, null=True, on_delete=models.SET_NULL)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Activity(models.Model):
    description = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    date_of = models.DateField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Activities'

class TodoItem(models.Model):
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    date_assigned = models.DateField(default=date.today, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    # assignedTo = models.ManyToManyField(ParentalUnit, related_name='assigned_to')
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.description

# class TodoItemAssignedTo(models.Model):
#     item = models.ForeignKey(TodoItem, null=False, on_delete=models.CASCADE)
#     assignedTo = models.ForeignKey(ParentalUnit, null=False, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.item.description

class Message(models.Model):
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    messageBody = models.TextField()
    dateAndTimeOf = models.DateTimeField(auto_now_add=True)
    recipients = models.ManyToManyField(ParentalUnit, related_name='recipients_of')

    def __str__(self):
        return self.messageBody

# class MessageTo(models.Model):
#     message = models.ForeignKey(Message, null=False, on_delete=models.CASCADE)
#     parentalunit = models.ForeignKey(ParentalUnit, null=False, on_delete=models.CASCADE)

class TeamMember(models.Model):
    fullname = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    imagename = models.CharField(max_length=150)

    def __str__(self):
        return self.fullname