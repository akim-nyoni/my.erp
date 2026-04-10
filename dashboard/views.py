from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

@login_required
def dashboard(request):
    return HttpResponse("Dashboard")