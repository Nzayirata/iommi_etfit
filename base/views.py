from django.utils.translation import gettext as _
from base.models import User, Workout, Exercise, BodyMeasurement

from iommi import (
    Action,
    Column,
    Form,
    html,
    Menu,
    MenuItem,
    Page,
    Table,
    LAST,
)


# Menu -----------------------------
class TopMenu(Menu):
    home = MenuItem(url="/", display_name=_("Home"))
    users = MenuItem(url="/users", display_name=_("Users"))
    workouts = MenuItem(url="/workouts", display_name=_("Workouts"))
    exercises = MenuItem(url="/exercises", display_name=_("Exercises"))
    body_measurements = MenuItem(url="/measurements", display_name=_("Body measurements"))

    class Meta:
        attrs__class = {"fixed-top": True}


# Tables ---------------------------
class UserTable(Table):
    class Meta:
        auto__model = User
        page_size = 10
        columns__username__cell__url = lambda row, **_: row.get_absolute_url()
        columns__username__filter__include = True
        columns__first_name__filter__include = True
        columns__last_name__filter__include = True
        columns__gender__filter__include = True
        columns__language__filter__include = True
        columns__email__filter__include = True
        columns__phone_number__filter__include = True
        columns__edit = Column.edit()
        columns__delete = Column.delete()
        actions__create_user = Action(attrs__href="/user-create/", display_name=_("Create user"))


class WorkoutTable(Table):
    class Meta:
        auto__model = Workout
        page_size = 10
        columns__name__cell__url = lambda row, **_: row.get_absolute_url()
        columns__name__filter__include = True
        columns__user__filter__include = True
        columns__edit = Column.edit()
        columns__delete = Column.delete()
        actions__create_workout = Action(attrs__href="/workout-create/", display_name=_("Create workout"))


class ExerciseTable(Table):
    class Meta:
        auto__model = Exercise
        page_size = 10
        auto__rows = Exercise.objects.all().select_related('workout__user')
        columns__name__filter__include = True
        columns__workout__filter__include = True
        columns__edit = Column.edit()
        columns__delete = Column.delete()
        actions__create_workout = Action(attrs__href="/exercise-create/", display_name=_("Create exercise"))


class BodyMeasurementTable(Table):
    class Meta:
        auto__model = BodyMeasurement
        page_size = 10
        columns__created__cell__url = lambda row, **_: row.get_absolute_url()
        columns__created__filter__include = True
        columns__user__filter__include = True
        columns__delete = Column.delete()
        actions__create_workout = Action(attrs__href="/measurement-create/", display_name=_("Create body measurement"))


# Pages ----------------------------
class HomePage(Page):
    menu = TopMenu()

    title = html.h1(_("ETFIT"))
    welcome_text = html.div(_("Best workout in town!"))
    body = html.body(
        html.br(),
        html.hr(),
        html.br(),
    )
    footer = html.div(
        html.br(),
        html.hr(),
        html.br(),
        html.br(),
        after=LAST,
    )

    users = UserTable(page_size=5)
    workouts = WorkoutTable(page_size=5)
    exercises = ExerciseTable(page_size=5)
    body_measurements = BodyMeasurementTable(page_size=5)


class UsersPage(Page):
    menu = TopMenu()

    users = UserTable(auto__model=User)


class UserPage(Page):
    menu = TopMenu()

    title = html.h1(lambda params, **_: params.username)

    workouts = WorkoutTable(auto__model=Workout, rows=lambda params, **_: Workout.objects.filter(user__username=params.username))
    exercises = ExerciseTable(auto__model=Exercise, rows=lambda params, **_: Exercise.objects.filter(workout__user__username=params.username))
    body_measurements = BodyMeasurementTable(auto__model=BodyMeasurement, rows=lambda params, **_: BodyMeasurement.objects.filter(user__username=params.username))


class CreateUserPage(Page):
    menu = TopMenu()

    form = Form.create(auto__model=User, extra__redirect_to="/")


class EditUserPage(Page):
    menu = TopMenu()

    form = Form.edit(auto__model=User, instance=lambda params, **_: User.objects.get(username=params.username), extra__redirect_to="/")


class DeleteUserPage(Page):
    menu = TopMenu()

    form = Form.delete(auto__model=User, instance=lambda params, **_: User.objects.get(username=params.username), extra__redirect_to="/")


class WorkoutsPage(Page):
    menu = TopMenu()

    users = WorkoutTable(auto__model=Workout)

class WorkoutPage(Page):
    menu = TopMenu()

    title = html.h1(lambda params, **_: params.workout_name)
    exercises = ExerciseTable(
        auto__model=Exercise,
        rows=lambda params, **_: Exercise.objects.filter(workout__name=params.workout_name),
        columns__workout__include=False,
    )


class CreateWorkoutPage(Page):
    menu = TopMenu()

    form = Form.create(auto__model=Workout, extra__redirect_to="/")


class EditWorkoutPage(Page):
    menu = TopMenu()

    form = Form.edit(auto__model=Workout, instance=lambda params, **_: Workout.objects.get(name=params.workout_name), extra__redirect_to="/")


class DeleteWorkoutPage(Page):
    menu = TopMenu()

    form = Form.delete(auto__model=Workout, instance=lambda params, **_: Workout.objects.get(name=params.workout_name), extra__redirect_to="/")


class ExercisesPage(Page):
    menu = TopMenu()

    users = ExerciseTable(auto__model=Exercise)


class CreateExercisePage(Page):
    menu = TopMenu()

    form = Form.create(auto__model=Exercise, extra__redirect_to="/")


class EditExercisePage(Page):
    menu = TopMenu()

    form = Form.edit(auto__model=Exercise, instance=lambda params, **_: Exercise.objects.get(name=params.exercise_name), extra__redirect_to="/")


class DeleteExercisePage(Page):
    menu = TopMenu()

    form = Form.delete(auto__model=Exercise, instance=lambda params, **_: Exercise.objects.get(name=params.exercise_name), extra__redirect_to="/")


class BodyMeasurementsPage(Page):
    menu = TopMenu()

    users = BodyMeasurementTable(auto__model=BodyMeasurement)


class BodyMeasurementPage(Page):
    menu = TopMenu()

    title = html.h1(lambda params, **_: params.body_measurement_date)
    body_text = 'Welcome to my iommi site...'

    exercises = BodyMeasurementTable(
        auto__model=BodyMeasurement,
        rows=lambda params, **_: BodyMeasurement.objects.filter(workout__name=params.body_measurement_date),
        columns__workout__include=False,
    )


class CreateBodyMeasurementPage(Page):
    menu = TopMenu()

    form = Form.create(auto__model=BodyMeasurement, extra__redirect_to="/")


class DeleteBodyMeasurementPage(Page):
    menu = TopMenu()

    form = Form.delete(auto__model=BodyMeasurement, instance=lambda params, **_: BodyMeasurement.objects.get(name=params.body_measurement_date), extra__redirect_to="/")
