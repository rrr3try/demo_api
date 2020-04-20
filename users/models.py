from django.db import models


class Human(models.Model):
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    avatar = models.FileField()
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    age = models.SmallIntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
