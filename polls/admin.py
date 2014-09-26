from django.contrib import admin
# here we are importing polls folder then read its file 
# model.py in this i have getting Question class 
from polls.models import Choice,Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)