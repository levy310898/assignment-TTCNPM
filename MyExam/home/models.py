from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):
    key = models.ForeignKey( User ,on_delete = models.CASCADE)
    examName = models.CharField(max_length= 200, default= "")

    def __str__(self):
        return self.examName

class Question(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)
    question = models.TextField(default= "")
    answerA = models.TextField(default= "")
    answerB = models.TextField(default= "")
    answerC = models.TextField(default= "")
    answerD = models.TextField(default= "")
    corrAns = models.CharField(max_length=1,default="")

    name = "{} | {} | {} | {} | {} | {}"
    def __str__(self):
        return self.name.format(self.question, self.answerA, self.answerB, self.answerC, self.answerD, self.corrAns)

class Point(models.Model):
    key1 = models.ForeignKey(User, on_delete = models.CASCADE)
    key2 = models.ForeignKey(Exam, on_delete= models.CASCADE)
    point = models.DecimalField(max_digits= 4, decimal_places= 2, default= 0)

    name = "Ng lam bai: {}, Bai: {}, Diem: {}"
    def __str__(self):
        return self.name.format(self.key1, self.key2, self.point)

class Info(models.Model):
    sex = models.TextField(max_length=6, default="")
    key = models.ForeignKey( User ,on_delete = models.CASCADE)
    birthDate = models.DateField(null= True)
    address = models.TextField(max_length=100, default="")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    name = "Info of {}"
    def __str__(self):
        return self.name.format(self.key)