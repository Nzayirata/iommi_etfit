from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import datetime


class Gender(models.TextChoices):
    MALE = "male"
    FEMALE = "female"


class Language(models.TextChoices):
    EN = "English"
    FR = "French"
    RW = "Kinyarwanda"
    SW = "Swahili"


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.MALE)
    height = models.PositiveSmallIntegerField()
    language = models.CharField(max_length=20 , choices=Language.choices, default=Language.EN)

    email = models.EmailField(unique=True)
    phone_number = models.PositiveIntegerField()
    # street = models.CharField(max_length=100, blank=True, null=True)
    # house_number = models.PositiveSmallIntegerField(blank=True, null=True)
    # city = models.CharField(max_length=50, blank=True, null=True)
    # zip = models.PositiveSmallIntegerField(blank=True, null=True)
    # country = models.CharField(max_length=50, blank=True, null=True)

    # is_trainer = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f"/user/{self}/"


class Workout(models.Model):
    name = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/user/{self.user}/{self}/"


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    reps = models.PositiveBigIntegerField()
    set = models.PositiveSmallIntegerField()
    rest_time = models.PositiveSmallIntegerField()

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")

    class Meta:
        unique_together = ["name", "workout"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/user/{self.workout.user}/{self.workout}/{self}/"


class BodyMeasurement(models.Model):
    created = models.DateTimeField(null=True, blank=True)
    weight = models.FloatField()
    muscle_mass = models.FloatField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="body_measurements")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return f"/user/{self.user}/{self}/"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        super(BodyMeasurement, self).save(*args, **kwargs)
        return self
