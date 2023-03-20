import logging
from base.models import User, Workout, Exercise, Gender, Language
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


USERS_DATA = [
    ["user_01", "Peter", "Kagame", "1998-08-12", Gender.MALE, 170, Language.EN, "peterkagame@gmail.com", 788847234],
    ["user_02", "David", "Kagame", "1996-09-13", Gender.MALE, 175, Language.EN, "davidkagame@gmail.com", 789847234]
]
EXERCISES_DATA = [
    ["pull up", 20, 3, 30],
    ["squat", 20, 3, 30],
    ["russian twist", 20, 3, 30],
    ["dip", 20, 3, 30],
    ["lunges", 20, 3, 30],
    ["barbell squat", 10, 3, 60],
    ["bumbbell power clean", 20, 3, 30],
    ["push jerk", 10, 3, 60],
    ["ring musle up", 20, 3, 60],
]
WORKOUTS_DATA = [
    ["Monday workout", "user_01", ["pull up", "squat", "push jerk", "lunges"]],
    ["Tuesday workout", "user_01", ["lunges", "dip", "bumbbell power clean"]],
    ["Wednesday workout", "user_01", ["ring musle up", "barbell squat", "lunges", "bumbbell power clean"]],
    ["Thursday workout", "user_02", ["barbell squat", "lunges", "dip", "bumbbell power clean"]],
    ["Friday workout", "user_02", ["barbell squat", "lunges", "dip"]],
]

PPPPP = [
    ["pull up", "squat", "push jerk", "lunges"],
    ["lunges", "dip", "bumbbell power clean"],
    ["ring musle up", "barbell squat", "lunges", "bumbbell power clean"],
    ["barbell squat", "lunges", "dip", "bumbbell power clean"],
    ["barbell squat", "lunges", "dip"],
]

def _create_users():
    user_objs = [
        User(
            username=user[0],
            first_name=user[1],
            last_name=user[2],
            date_of_birth=user[3],
            gender=user[4],
            height=user[5],
            language=user[6],
            email=user[7],
            phone_number=user[8]
        ) for user in USERS_DATA
    ]
    return User.objects.bulk_create(user_objs)

def _create_exercises():
    exercises_objs = [
        Exercise(
            name=exercise[0],
            reps=exercise[1],
            set=exercise[2],
            rest_time=exercise[3],
        ) for exercise in EXERCISES_DATA
    ]
    return Exercise.objects.bulk_create(exercises_objs)

def _create_workouts():
    workout_objs = [
        Workout(
            name=workout[0],
            user=User.objects.get(username=workout[1]),
            exercises=Exercise.get(name=workout[2])
        ) for workout in WORKOUTS_DATA
    ]
    created_objs = Workout.objects.bulk_create(workout_objs)
    import pdb;pdb.set_trace()

    for i, obj in enumerate(created_objs):
        obj.exercises.set(Exercise.objects.filter(name__in=PPPPP[i]))





class Command(BaseCommand):
    help = "Populate DB"

    def handle(self, *args, **options):
        User.objects.all().delete()
        logger.info("Users deleted!")
        Workout.objects.all().delete()
        logger.info("Workouts deleted!")
        Exercise.objects.all().delete()
        logger.info("Exercises deleted!")

        # try:
        #     _create_users()
        #     logger.info("Users created!")
        #     _create_exercises()
        #     logger.info("Exercises created!")
        #     _create_workoutss()
        #     logger.info("Workouts created!")
        # except Exception as e:
        #     logger.warning(f"Failed!")

        # _create_users()
        # _create_exercises()
        # _create_workouts()
        logger.info("All good!")

