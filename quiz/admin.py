from django.contrib import admin
from .models import *
from django.db.models import Sum

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ("quiz",)

class UserResponseAdmin (admin.ModelAdmin):
    list_display = ("user", "question", "answer", "correct", "quiz_title", "quiz_total_correct") 
    search_fields = ("user_ _username",)
    list_filter = ("user", "quiz")

    def quiz_title(self, obj):
        return obj.quiz.title
    
    def correct(self, obj):
        return obj.answer.correct if obj.answer else 0
    
    def quiz_total_correct(self, obj):
        user_responses = UserResponse.objects.filter(user=obj.user, quiz=obj.quiz)
        total = user_responses.aggregate(total_correct= Sum('answer__correct')) ["total_correct"] 
        return total if total is not None else 0
    

admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Person)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
