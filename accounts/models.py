from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey, PositiveSmallIntegerField, Model, DO_NOTHING, CharField


# Create your models here.

class Gender(Model):
    gender = CharField(max_length=10)

    def __str__(self):
        return self.gender


class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    gender = ForeignKey(Gender, on_delete=DO_NOTHING, null=True, blank=True)
    height_cm = PositiveSmallIntegerField(null=True, blank=True)
    weight_kg = PositiveSmallIntegerField(null=True, blank=True)
    squat_record_kg = PositiveSmallIntegerField(null=True, blank=True)
    dead_lift_record_kg = PositiveSmallIntegerField(null=True, blank=True)
    bench_press_record_kg = PositiveSmallIntegerField(null=True, blank=True)
    pull_up_record_amount = PositiveSmallIntegerField(null=True, blank=True)
    dips_record_amount = PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.username}'


class Trainer(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True)
    ppl_on_training = models.ManyToManyField(User, related_name='primary_key', blank=True)
    number_of_training_ppl = PositiveSmallIntegerField(default=0, blank=True)
    number_of_plans_made = PositiveSmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.user}'
