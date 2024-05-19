from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def index(request):
    images1 = Person.objects.all()[:3]
    images2 = Person.objects.all()[3:6]
    images3 = Person.objects.all()[6:]
    context ={"images1":images1, "images2":images2, "images3": images3}
    return render(request, 'index.html', context)

def quiz(request):
    quizzes = Quiz.objects.filter(public=True)
    context = {"quizzes": quizzes}
    return render(request, 'quiz_choice.html', context=context)


def quiz_details(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    context = {"quiz":quiz, "questions":questions}
    return render(request, "quiz.html", context)


def details(request, name):
    luminary = get_object_or_404(Person, name=name)
    return render(request, 'details.html', {'luminary': luminary})