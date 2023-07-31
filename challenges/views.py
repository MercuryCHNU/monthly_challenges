from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.


# def january(request):
#     return HttpResponse("Good job comrade!(≖_≖ )")


# def february(request):
#     return HttpResponse("👋≧◉ᴥ◉≦ Today is June. Why February?")


# def march(request):
#     return HttpResponse("(͠≖ ͜ʖ͠≖)👌 OMG ITS A PIZZA")

monthly_challenges = {
    "january": "Good job comrade!(≖_≖ )",
    "february": "👋≧◉ᴥ◉≦ Today is June. Why February?",
    "march": "(͠≖ ͜ʖ͠≖)👌 OMG ITS A PIZZA",
    "april": "Good job comrade!(≖_≖ )",
    "may": "Good job comrade!(≖_≖ )",
    "june": "Good job comrade!(≖_≖ )",
    "july": "Good job comrade!(≖_≖ )",
    "august": "Good job comrade!(≖_≖ )",
    "september": "Good job comrade!(≖_≖ )",
    "october": "Good job comrade!(≖_≖ )",
    "novebmer": "Good job comrade!(≖_≖ )",
    "december": None
}

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month_challenge", args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound(
            "Welcome to the end of this WebSite (👍≖‿‿≖)👍 👍(≖‿‿≖👍)"
        )

    redirect_month = months[month - 1]  # Rozpochinaet'sya z nulya
    redirect_path = reverse(
        "month_challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "Good job comrade!(≖_≖ )"
#     elif month == "february":
#         challenge_text = "👋≧◉ᴥ◉≦ Today is June. Why February?"
#     elif month == "march":
#         challenge_text = "(͠≖ ͜ʖ͠≖)👌 OMG ITS A PIZZA"
#     else:
#         return HttpResponseNotFound("Very bad page")
#     return HttpResponse(challenge_text)
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenge.html")      #f"<h1>{challenge_text}</h1>"
        # return HttpResponse(response_data)
    except:
        raise Http404()
