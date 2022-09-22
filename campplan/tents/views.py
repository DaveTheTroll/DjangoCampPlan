from django.shortcuts import render
from django.http import HttpResponse
from tents.models import *

def index(request):
    return HttpResponse("Hello camper.")

def nations(request):
    nations = Nation.objects.order_by("id")
    output = "<br/>".join(["<a href='nation/%d'>%s</a>"%(n.id,n.name) for n in nations])
    return HttpResponse(output)

def nation(request, id):
    return HttpResponse("Nation %d"%(id))