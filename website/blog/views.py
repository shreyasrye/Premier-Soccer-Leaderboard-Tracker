from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, UserTeams

# Create your views here.
def home(request):
    if request.method == "POST":
        print(request.POST)
        if "create_team" in request.POST:
            # do stuff to create the team
            Team.objects.create(name=team1)
        elif "add_match" in request.POST:
            # do stuff to update team standings
            print()
        else:
            # unexpected error
            return HttpResponse("<h1>About</h1>")

        team1 = request.POST["team1"]
    return render(request, "blog/select_league.html")


def about(request):
    return HttpResponse("<h1>About</h1>")

