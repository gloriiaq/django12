from django.shortcuts import render

# Create your views here.


def showcase(request):
    return render(request, "showcase/showcases.html")


def static(request):
    return render(request, "showcase/index.html")
