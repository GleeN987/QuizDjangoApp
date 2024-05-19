from django.contrib import admin
from .models import *

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ("quiz",)

admin.site.register(Person)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
