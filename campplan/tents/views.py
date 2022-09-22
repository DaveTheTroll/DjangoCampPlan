from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from tents.models import *

def index(request):
    return HttpResponse("Hello camper.")

def nations(request):
    nation_list = Nation.objects.order_by("id")
    return render(request, "tents/nations.html", {"nation_list": nation_list})

def nation(request, id):
    try:
        nation = Nation.objects.get(id=id)
    except:
        raise Http404("Nation does not exist")
    return render(request, "tents/nation.html", {"nation": nation})