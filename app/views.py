# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from app.models import Task
from app.utils import getTasks


# Create your views here.
def redirectToVue(request, *args, **kwargs):
    return render(request, 'vue.html')


def dynamic_files(request, ftype):
    if ftype == 'js':
        content_type = 'text/javascript'

    elif ftype == 'css':
        content_type = 'text/css'

    return render(request, 'dynamic.' + ftype, {}, content_type=content_type)


def tasks(request, *args, **kwargs):
    if request.is_ajax():
        if 'createToDo' in request.GET:
            try:
                toDo = Task()
                toDo.name = request.GET['label']
                toDo.quad = request.GET['quad']
                toDo.save()
                return JsonResponse({'msgType': 'success', 'msg': 'Created to-do item successfully.'})
            except Exception:
                return JsonResponse({'msgType': 'error', 'msg': 'Failed to create to-do item. Please try again later.'})
        if 'renameTodo' in request.GET:
            try:
                toDo = Task.objects.get(id=int(request.GET['todoId']))
                toDo.name = request.GET['newLabel']
                toDo.save()
                return JsonResponse({'msgType': 'success', 'msg': 'Renamed to-do item successfully.'})
            except Exception:
                return JsonResponse({'msgType': 'error', 'msg': 'Failed to rename to-do item. Please try again later.'})
        if 'delToDo' in request.GET:
            try:
                toDo = Task.objects.get(id=int(request.GET['delToDo']))
                toDo.delete()
                return JsonResponse({'msgType': 'success', 'msg': 'Deleted to-do item successfully.'})
            except Exception:
                return JsonResponse({'msgType': 'error', 'msg': 'Failed to delete to-do item. Please try again later.'})
        if 'saveToDoOrder' in request.GET:
            try:
                quad0OrderedIds = request.GET['quad0Order'].strip().split(',')
                quad1OrderedIds = request.GET['quad1Order'].strip().split(',')
                quad2OrderedIds = request.GET['quad2Order'].strip().split(',')
                quad3OrderedIds = request.GET['quad3Order'].strip().split(',')

                orderVal = 1
                for orderedId in quad0OrderedIds:
                    if orderedId.strip() != '':
                        todoItem = Task.objects.get(id=int(orderedId.strip()))
                        todoItem.ordering = orderVal
                        todoItem.quad = 0
                        todoItem.save()
                        orderVal += 1

                orderVal = 1
                for orderedId in quad1OrderedIds:
                    if orderedId.strip() != '':
                        todoItem = Task.objects.get(id=int(orderedId.strip()))
                        todoItem.ordering = orderVal
                        todoItem.quad = 1
                        todoItem.save()
                        orderVal += 1

                orderVal = 1
                for orderedId in quad2OrderedIds:
                    if orderedId.strip() != '':
                        todoItem = Task.objects.get(id=int(orderedId.strip()))
                        todoItem.ordering = orderVal
                        todoItem.quad = 2
                        todoItem.save()
                        orderVal += 1

                orderVal = 1
                for orderedId in quad3OrderedIds:
                    if orderedId.strip() != '':
                        todoItem = Task.objects.get(id=int(orderedId.strip()))
                        todoItem.ordering = orderVal
                        todoItem.quad = 3
                        todoItem.save()
                        orderVal += 1

                return JsonResponse({'msgType': 'success', 'msg': 'Saved to-do items order successfully.'})
            except Exception:
                return JsonResponse({'msgType': 'error', 'msg': 'Failed to save task order. Please try again later.'})

    context = {
        'location': "To-Do",
        'page_title': "Tasks",
        'no_sidebar': True,
        'quad0Items': getTasks(0),
        'quad1Items': getTasks(1),
        'quad2Items': getTasks(2),
        'quad3Items': getTasks(3),
    }
    return render(request, 'tasks.html', context)
