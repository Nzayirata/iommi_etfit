from django.urls import path
from base import views


app_name = "base"

urlpatterns = [
    path("", views.HomePage().as_view(), name="home"),

    path('users/', views.UsersPage().as_view()),
    path('user/<username>/', views.UserPage().as_view()),
    path('user-create/', views.CreateUserPage().as_view()),
    path('user/<username>/edit/', views.EditUserPage().as_view()),
    path('user/<username>/delete/', views.DeleteUserPage().as_view()),

    path('workouts/', views.WorkoutsPage().as_view()),
    path('user/<username>/<workout_name>/', views.WorkoutPage().as_view()),
    path('workout-create/', views.CreateWorkoutPage().as_view()),
    path('user/<username>/<workout_name>/edit/', views.EditWorkoutPage().as_view()),
    path('user/<username>/<workout_name>/delete/', views.DeleteWorkoutPage().as_view()),

    path('exercises/', views.ExercisesPage().as_view()),
    path('exercise-create/', views.CreateExercisePage().as_view()),
    path('user/<username>/<workout_name>/<exercise_name>/edit/', views.EditExercisePage().as_view()),
    path('user/<username>/<workout_name>/<exercise_name>/delete/', views.DeleteExercisePage().as_view()),

    path('measurements/', views.BodyMeasurementsPage().as_view()),
    path('user/<username>/<body_measurement_date>/', views.BodyMeasurementPage().as_view()),
    path('measurement-create/', views.CreateBodyMeasurementPage().as_view()),
    path('user/<username>/<body_measurement_date>/delete/', views.DeleteBodyMeasurementPage().as_view()),
]
