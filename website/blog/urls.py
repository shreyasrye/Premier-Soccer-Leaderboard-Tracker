from django.urls import path
from . import views

urlpatterns = [
    path("league/<int:league_id>/", views.league, name="league"),
    path("", views.landing, name="landing"),
]
