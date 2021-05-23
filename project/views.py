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

from cuckoo import *

# A persistent data storage thingy
table = Cuckoo()

def index(request):
    return render(request, "index.html")



