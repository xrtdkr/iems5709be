from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from be.models import Productions, Categories
from utils import *


def hello(request):
    return JsonResponse({"msg": "hello"})


@require_GET
def get_categories(request):
    ret = []
    for category in Categories.objects.all():
        ret.append({"id": category.id, "name": category.name})
    return JsonResponse(assemble_success_msg(ret))


@require_GET
def get_production_by_id(request):
    ret = []
    c_id = request.GET['id']

    for production in Productions.objects.filter(category_id=c_id):
        ret.append(production.get_production())

    return JsonResponse(
        assemble_success_msg(ret)
    )




# Create your views here.
