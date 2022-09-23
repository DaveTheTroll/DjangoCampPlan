from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from tents.models import *

def index(request):
    return render(request, "tents/index.html")

def nations(request):
    nation_list = Nation.objects.order_by("id")
    return render(request, "tents/nations.html", {"nation_list": nation_list})

def nation(request, id):
    nation = get_object_or_404(Nation, id=id)
    return render(request, "tents/nation.html", {"nation": nation})