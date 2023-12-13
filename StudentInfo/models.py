from django.db import models

# Create your models here.


class Grade (models.Model):
    Grade = models.CharField(max_length=100)

    def __str__(self):
        return self.Grade


class Students(models.Model):
    Name = models.CharField(max_length=100)
    Roll = models.IntegerField()
    City = models.CharField(max_length=100)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
