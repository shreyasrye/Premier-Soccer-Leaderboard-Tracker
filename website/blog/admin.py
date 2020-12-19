from django.contrib import admin
from .models import League, Team, UserTeams

# Register your models here.
models = [League, Team, UserTeams]

for model in models:
    admin.site.register(model)
