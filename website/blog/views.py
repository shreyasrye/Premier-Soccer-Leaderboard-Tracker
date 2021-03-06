from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Team, UserTeams, League
from django.contrib.auth.decorators import login_required


@login_required
def league(request, league_id):
    if request.method == "POST":
        if "create_team" in request.POST:
            Team.objects.create(name=team1)
        elif "add_match" in request.POST:
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
            return HttpResponse("<h1>About</h1>")
    league = League.objects.get(id=league_id)
    teams = Team.objects.filter(league=league)
    teams = sorted(teams, key= lambda t: t.points())
    users = []
    for team in teams:
        members = UserTeams.objects.filter(team=team)
        users.append(members)
    context = {
        "league": league,
        "teams": teams,
        "users": users,
        "is_admin": request.user == league.creator,
    }
    return render(request, "blog/select_league.html", context)


@login_required
def landing(request):
    if request.method == "POST":
        if "league-name" in request.POST:
            league = League.objects.create(
                name=request.POST["league-name"], creator=request.user
            )
            return redirect("league", league_id=league.id)
        elif "league-code" in request.POST:
            team = Team.objects.get(code=request.POST["league-code"])
            UserTeams.objects.create(team=team, user=request.user)
            return redirect("league", league_id=team.league.id)
        else:
            return False
    userteams = request.user.userteams_set.all()
    context = {"userteams": userteams}
    return render(request, "blog/landing_page.html", context)

