from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    images = Person.objects.all()
    images1 = Person.objects.all()[:3]
    images2 = Person.objects.all()[3:6]
    images3 = Person.objects.all()[6:]
    context ={"images": images,"images1":images1, "images2":images2, "images3": images3}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def quiz(request):
    quizzes = Quiz.objects.filter(public=True)
    context = {"quizzes": quizzes}
    return render(request, 'quiz_choice.html', context=context)


def quiz_details(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    context = {"quiz":quiz, "questions":questions}
    return render(request, "quiz.html", context)


@login_required(login_url='login')
def quiz_submit(request, quiz_id):
    if request.method == "POST":
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        error = None
        
        for question in questions:
            answer_id = request.POST.get(f"question_{question.id}", None)
            if answer_id:
                answer = get_object_or_404(Answer, id=answer_id)
                UserResponse.objects.create(
                    user=request.user,
                    quiz=quiz,
                    question=question,
                    answer=answer
                )
            else:
                error = "Answer all questions"
        if error:
            messages.error(request, error)
            context = {"quiz":quiz, "questions":questions}
            return render(request, "quiz.html", context)
        messages.success(request, "Quiz submitted")
        return redirect("quizzes")
    return redirect("quiz_details", quiz_id=quiz_id)



def details(request, name):
    luminary = get_object_or_404(Person, name=name)
    return render(request, 'details.html', {'luminary': luminary})