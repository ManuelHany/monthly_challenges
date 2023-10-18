from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from collections import OrderedDict
from django.urls import reverse


monthly_challenges = OrderedDict({
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "This is may!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Eat no meat for the entire month!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Eat no meat for the entire month!",
    "december": "Walk for at least 20 minutes every day!"
})


# Create your views here.
def index(request):

    list_items = ""
    months  = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalud month")
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


# the second argument (month) must be the same as the one inside the <>
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month.capitalize(),
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
