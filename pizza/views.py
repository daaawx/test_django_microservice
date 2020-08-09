import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from pizza.models import Pizza


def index(request, pid):
    pizza = get_object_or_404(Pizza, id=pid)
    return JsonResponse({
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description,
    })


def random_pizza(request):
    c = Pizza.objects.count()
    pizza = Pizza.objects.all()[random.randint(0, c - 1)]
    return JsonResponse({
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description,
    })
