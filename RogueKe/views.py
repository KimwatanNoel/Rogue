from django.shortcuts import render
from .models import Home
from .models import Fashion
from .models import Technology
from .models import Lifestyle
from .models import Man_Talk
from .models import Trending
from .models import Sports


def index_view(request):
    home_items = Home.objects.all()

    context = {
        "home_items": home_items,
    }

    return render(request, "blog/index.html", context)


def fashion_view(request):
    fashion_items = Fashion.objects.all()

    context = {
        "fashion_items": fashion_items,
    }

    return render(request, "blog/fashionpage.html", context)



def technology_view(request):
    tech_items = Technology.objects.all()

    context = {
        "tech_items": tech_items,
    }

    return render(request, "blog/techpage.html", context)


def lifestyle_view(request):
    life_items = Lifestyle.objects.all()

    context = {
        "life_items": life_items,
    }

    return render(request, "blog/lifestylepage.html", context)

def man_view(request):
    man_items = Man_Talk.objects.all()

    context = {
        "man_items": man_items,
    }

    return render(request, "blog/mantalkpage.html", context)


def trend_view(request):
    trend_items = Trending.objects.all()

    context = {
        "trend_items": trend_items,
    }

    return render(request, "blog/trendingpage.html", context)


def sports_view(request):
    sports_item = Sports.objects.all()

    context = {
        "sports_items": sports_item,
    }

    return render(request, "blog/sportspage.html", context)


