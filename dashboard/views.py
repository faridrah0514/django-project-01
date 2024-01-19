from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("coba dulu")

def super_dashboard(request):
    return render(request, 'dashboard/index.html')