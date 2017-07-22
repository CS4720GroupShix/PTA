from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classinfo = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class ParentalUnit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_assigned = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.teacher.user.username + ' ' + self.title

    class Meta:
        verbose_name_plural = 'Homework'

class WishlistItem(models.Model):
    description = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    parentalUnit = models.ForeignKey(ParentalUnit, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.description

class Activity(models.Model):
    description = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    date_of = models.DateTimeField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Activities'

class TodoItem(models.Model):
    description = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    assignedTo = models.ManyToManyField(ParentalUnit, related_name='assigned_to')

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
    dateOf = models.DateTimeField(auto_now_add=True)
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