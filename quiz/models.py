from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=200)
    level = models.IntegerField()
    op1 = models.CharField(max_length=50)
    op2 = models.CharField(max_length=50)
    op3 = models.CharField(max_length=50)
    op4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.question

class Score(models.Model):
    playerName = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="score")
    points = models.IntegerField()

    def __str__(self) -> str:
        return self.playerName

class ScoreBoard(models.Model):
    playerName = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="scoreboard")
    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name="scoreboard")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.playerName