from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("league/<int:league_id>/", views.league, name="league"),
    path("soccer/", views.landing, name="landing"),
    path("", admin.site.urls),
]
