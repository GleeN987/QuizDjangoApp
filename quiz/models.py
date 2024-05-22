from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "People"


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete = models.CASCADE)

    def __str__(self):
        return self.text
    

class Answer(models.Model):
    text = models.CharField(max_length=200)
    Question = models.ForeignKey(Question, related_name="answers", on_delete = models.CASCADE)
    correct = models.FloatField(default=0)

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: Quiz {self.quiz.title}, Question {self.question.text}, Answer {self.answer.text}"
    
    def quiz_score(self):
        total_score = sum(answer.correct for answer in self.question.answer.all())
        return total_score