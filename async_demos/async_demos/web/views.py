import time

from django.http import JsonResponse
from django.shortcuts import render
from django import views

from async_demos.web.tasks import slow_task


class SlowTaskView(views.View):
    def get(self, request, is_slow):
        start = time.time()
        if is_slow:
            slow_task(5)
        else:
            slow_task.delay(5)
        end = time.time()
        return JsonResponse(data={
            'time_executed': end - start,
        })
