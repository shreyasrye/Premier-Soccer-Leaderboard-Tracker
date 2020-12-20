from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, UserTeams, League

# Create your views here.
def league(request, league_id):
    if request.method == "POST":
        if "create_team" in request.POST:
            # do stuff to create the team
            Team.objects.create(name=team1)
        elif "add_match" in request.POST:
            # do stuff to update team standings
            leagueName = request.POST["league"]
            team1name = request.POST["team1"]
            team1goals = request.POST["team1goals"]
            team2name = request.POST["team2"]
            team2goals = request.POST["team2goals"]

            league = League.objects.get(id=league_id)
            team1 = Team.objects.get(name=team1name, league=league)
            team2 = Team.objects.get(name=team2name, league=league)

            if team1goals > team2goals:
                team1.wins += 1
                team2.losses -= 1
            elif team1goals < team2goals:
                team2.wins += 1
                team1.losses -= 1
            else:
                team1.draws += 1
                team2.draws += 1

            team1.goals_for += team1goals
            team2.goals_for += team2goals
            team1.goals_against += team2goals
            team2.goals_against += team1goals

            team1.save()
            team2.save()

            return True

        else:
            # unexpected error
            return HttpResponse("<h1>About</h1>")

    return render(request, "blog/select_league.html")


def about(request):
    return HttpResponse("<h1>About</h1>")

