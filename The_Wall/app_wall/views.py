from django.shortcuts import render, redirect, HttpResponse
from  .models import *
# Create your views here.

def wall(request):
    return HttpResponse('Hi Human')
    # return render(request, 'wall.html')