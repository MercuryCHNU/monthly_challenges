from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    path("", views.index, name="index"), #/challenges/
    path("<str:month>", views.monthly_challenge, name="month_challenge"),
    path("<int:month>", views.monthly_challenge_by_number)
]
