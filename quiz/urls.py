from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("quizzes/", views.quiz, name="quizzes"),
    path("quizzes/<int:quiz_id>", views.quiz_details, name="quiz_details"),
    path("quizzes/<int:quiz_id>/submit", views.quiz_submit, name="quiz_submit"),
    path("details/<str:name>/", views.details, name="details")
]
