from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import datetime
from django.views.generic.list import BaseListView

# import hash tables
from cuckoo import *
from chaining import *

cuckoo = False

if cuckoo:
    employees = Cuckoo()
else:
    employees = ChainedDict()


employees = {}

import csv
with open('records.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

cols = data[0]
del data[0]

for entry in data:
    id = entry[0]
    employee_data = {}
    for i in range(1, len(cols) ):
        employee_data[cols[i]] = entry[i]
    employees[id] = employee_data



def index(request):
    return render(request, "index.html", {
        'employees': employees
    })


#---------------Login and Registering Views---------------#

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


