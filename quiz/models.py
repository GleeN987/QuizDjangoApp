from django.db import models

# Create your models here.
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