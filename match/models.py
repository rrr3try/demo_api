from django.db import models
from django.db.models.signals import post_save
from faker import Faker

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


def create_match(sender, instance, **kwargs):
    faker = Faker()
    gender_suffix = Human.GENDER_CHOICES[not instance.gender][1].lower()
    name = getattr(faker, f"name_{gender_suffix}")()
    name, second_name = name.split()[:2]
    Match(
        human_id=instance,
        first_name=name,
        second_name=second_name,
        gender=instance.gender,
        age=instance.age + faker.random_digit()
    ).save()


post_save.connect(create_match, sender=Human)
