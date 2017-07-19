# Register your models here.
from django.contrib import admin

from .models import Teacher, ParentalUnit, Homework, WishlistItem, \
    Activity, TodoItem, TodoItemAssignedTo, Message, MessageTo


class TeacherModel(admin.ModelAdmin):
    def firstname(self, instance):
        return instance.user.first_name

    def lastname(self, instance):
        return instance.user.last_name

    list_display = ('user', 'firstname', 'lastname')

class ParentalUnitModel(admin.ModelAdmin):
    def firstname(self, instance):
        return instance.user.first_name

    def lastname(self, instance):
        return instance.user.last_name

    list_display = ('user', 'firstname', 'lastname', 'teacher')

class HomeworkModel(admin.ModelAdmin):
    pass

class TodoAssigneesInline(admin.StackedInline):
    model = TodoItemAssignedTo

class TodoItemAdmin(admin.ModelAdmin):
    inlines = [TodoAssigneesInline]

class MessageToInline(admin.StackedInline):
    model = MessageTo

class MessageAdmin(admin.ModelAdmin):
    inlines = [MessageToInline]

admin.site.register(Teacher, TeacherModel)
admin.site.register(ParentalUnit, ParentalUnitModel)
admin.site.register(Homework, HomeworkModel)
admin.site.register(WishlistItem)
admin.site.register(Activity)
admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Message, MessageAdmin)

