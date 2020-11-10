from django.shortcuts import render
from django.http import HttpResponse
from .models import Bitcoin
import subprocess
import os


def index(request):
    schedule = os.environ.get("SCHEDULE", default='2')
    schedule_str = '*/' + str(schedule)

    debug = int(os.environ.get("DEBUG", default=0))
    debug_str = str(debug)

    context = {'schedule_str': schedule_str, 'debug_str': debug_str}
    return render(request, 'main/index.html', context=context)


def reset_celery(request):
    subprocess.check_call('celery multi restart -A kt w1 -l info', shell=True)
    Bitcoin.objects.all().delete()
    return HttpResponse("Celery reset")

