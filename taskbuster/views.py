# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


def home(request):
    today = datetime.date.today()
    return render(request, "taskbuster/index.html",
                  {'today': today,
                   'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
