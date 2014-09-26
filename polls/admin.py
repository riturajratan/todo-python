from django.contrib import admin
# here we are importing polls folder then read its file 
# model.py in this i have getting Question class 
from polls.models import Choice,Question
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):

		list_display = ('question_text', 'pub_date', 'was_published_recently')
		
		fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]

		list_filter = ['pub_date']
		
		search_fields = ['question_text']

		inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)