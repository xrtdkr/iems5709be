# coding: utf-8
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from be.models import Productions, Categories
from utils import *


def hello(request):
    return JsonResponse({"msg": "hello"})


@require_GET
def get_categories(request):
    '''
    :param request:
    :return: 返回所有已经有的category ids
    '''
    ret = []
    for category in Categories.objects.all():
        ret.append({"id": category.id, "name": category.name})
    return JsonResponse(assemble_success_msg(ret))


@require_POST
def add_categories(request):
    pass


@require_GET
def get_commodity_ids(request):
    '''
    :param request: [get] cid: category_id 类别id
    :return: 根据类别id返回所有commodity的id
    '''
    ret = []
    c_id = request.GET['id']

    for production in Productions.objects.filter(category_id=c_id):
        ret.append(production.id)

    return JsonResponse(assemble_success_msg(ret))


@require_GET
def get_production_by_id(request):
    '''
    :param request: [get] id: 类别id
    :return: 根据类别id返回类别下所有商品的所有信息
    '''
    ret = []
    c_id = request.GET['id']

    for production in Productions.objects.filter(category_id=c_id):
        ret.append(production.get_production())

    return JsonResponse(
        assemble_success_msg(ret)
    )


@require_GET
def get_commodity(request):
    '''
    :param request: [get] id: 商品id
    :return: 根据商品id返回商品信息
    '''
    ret = []
    commodity_id = request.GET['id']

    return JsonResponse(
        assemble_success_msg(Productions.objects.get(id=commodity_id).get_production())
    )

# Create your views here.j
