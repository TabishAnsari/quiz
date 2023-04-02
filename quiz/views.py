from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import random

from .models import  Questions, Score, User


# Create your views here.
def index(request):
    return render(request, "index.html")

def quiz_start(request):
    user = request.user
    if request.method == 'GET':
        questionsdata =  Questions.objects.all()
        payload = []
        for questiondata in questionsdata:
            payload.append({
                "question" :questiondata.question,
                "option1" : questiondata.op1,
                "option2" : questiondata.op2,
                "option3" : questiondata.op3,
                "option4" : questiondata.op4,
                "answer" : questiondata.answer,
            })
        random.shuffle(payload)
        payload = payload[:10]
        
    return JsonResponse({"payload" : payload })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")