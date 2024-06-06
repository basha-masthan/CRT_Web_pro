from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def school(request):
    roll = request.POST['roll']
    nmae = request.POST['nameofuser']
    return render(request,'school.html',{'roll':roll, 'name':nmae})

