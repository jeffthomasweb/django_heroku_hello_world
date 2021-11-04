
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='font-family: Arial; padding: 10%; text-align: center; font-size 4em'> Hello RocPy!🪨 🐍</h1>")
