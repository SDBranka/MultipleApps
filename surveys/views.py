from django.shortcuts import render, HttpResponse


def surveys(request):
    return HttpResponse("placeholder to display all the surveys created")

def new(request):
    return HttpResponse("placeholder for users to add a new survey")

