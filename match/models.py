from django.db import models

from users.models import Human


class Match(models.Model):
    human_id = models.ForeignKey(Human, on_delete=models.CASCADE)
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    age = models.SmallIntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)

