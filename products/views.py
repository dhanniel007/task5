from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def watercurls(request):
    return HttpResponse("<h1> Water Curls</h1>")
def bonestraight(request):
    return HttpResponse("<h1> Bone Straight</h1>")
def pinkycurls(request):
    return HttpResponse("<h1> Pinky Curls</h1>")  
def products(request):
    return HttpResponse("<h1> Product Page</h1>")