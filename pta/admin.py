# Register your models here.
from django.contrib import admin

from .models import Teacher, ParentalUnit, Homework, WishlistItem, \
    Activity, TodoItem, Message, TeamMember, HomeworkGrade

class ParentsInline(admin.StackedInline):
    model = ParentalUnit

class TeacherModel(admin.ModelAdmin):
    def firstname(self, instance):
        return instance.user.first_name

    def lastname(self, instance):
        return instance.user.last_name

    list_display = ('user', 'firstname', 'lastname')
    inlines = [ParentsInline]

class ParentalUnitModel(admin.ModelAdmin):
    def firstname(self, instance):
        return instance.user.first_name

    def lastname(self, instance):
        return instance.user.last_name

    list_display = ('user', 'firstname', 'lastname', 'teacher')

class HomeworkModel(admin.ModelAdmin):
    pass

# class TodoAssigneesInline(admin.StackedInline):
#     model = TodoItemAssignedTo

class TodoItemAdmin(admin.ModelAdmin):
    pass
#     inlines = [TodoAssigneesInline]
#
# class MessageToInline(admin.StackedInline):
#     model = MessageTo

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('dateAndTimeOf',)
    # inlines = [MessageToInline]

admin.site.register(Teacher, TeacherModel)
admin.site.register(ParentalUnit, ParentalUnitModel)
admin.site.register(Homework, HomeworkModel)
admin.site.register(WishlistItem)
admin.site.register(Activity)
admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(TeamMember)
admin.site.register(HomeworkGrade)
