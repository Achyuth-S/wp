from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    english_marks = models.IntegerField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
