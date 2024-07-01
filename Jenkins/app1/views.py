from django.shortcuts import render

# Create your views here.

def show(r):
    return render(r,"app1/show.html")