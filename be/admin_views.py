# coding: utf-8
from django.http import JsonResponse
from models import Categories

from utils import assemble_success_msg, assemble_fail_msg
from tools import TimeHandle
from views import get_categories
from models import Categories, Productions


def category_get(request):
    '''
    :param request:
    :return: get all the category
    @tested
    '''
    return get_categories(request)


def category_add(request):
    '''
    add a category
    :param request: paremeter: name description
    :return: msg
    @tested
    '''

    if request.method != "POST":
        return JsonResponse(assemble_fail_msg("error request method"))

    if ("name" in request.POST.keys()) and ("description" in request.POST.keys()):
        name = request.POST["name"]
        description = request.POST["description"]
        Categories.objects.create(name=name, description=description)
        return JsonResponse(assemble_success_msg("success"))

    else:
        return JsonResponse(assemble_fail_msg("lack of parameters"))


def category_delete(request):
    '''
    delete a category
    :param request: parameter: id(the id of category)
    :return: msg
    @tested
    '''

    if request.method != 'POST':
        return JsonResponse(assemble_fail_msg("error request method"))

    if "id" in request.POST.keys():
        category_id = request.POST["id"]
        Categories.objects.get(id=category_id).delete()
        return JsonResponse(assemble_success_msg("success"))
    else:
        JsonResponse(assemble_fail_msg("lack or wrong parameter"))


def category_update(request):
    '''
    update the category, method: post
    :param request: [mask_put post] parameters: id, name,s description
    :return:
    tested
    '''
    if request.method != "POST":
        return JsonResponse(assemble_fail_msg("error request method"))

    if ("id" in request.POST.keys()) and ("name" in request.POST.keys()) and ("description" in request.POST.keys()):
        category_id = request.POST["id"]
        category = Categories.objects.get(id=category_id)
        category.name = request.POST["name"]
        category.description = request.POST["description"]
        category.save()
        return JsonResponse(assemble_success_msg("success"))
    else:
        return JsonResponse(assemble_fail_msg("lack or wrong parameter"))


def production_get(request):
    '''
    :param request:
    :return: all productions info
    '''

    ret_list = []

    for producion in Productions.objects.all():
        ret_list.append(producion.get_production())

    return JsonResponse(assemble_success_msg(ret_list))


def production_add(request):
    '''
    add a production
    :param request: parameter: name, category_id, price, description, Image
    :return: msg
    @tested
    '''

    if request.method != "POST":
        return JsonResponse(assemble_fail_msg("error request method"))

    if ("name" in request.POST.keys()) \
            and ("category_id" in request.POST.keys()) \
            and ("price" in request.POST.keys()) \
            and ("description" in request.POST.keys()) \
            and ("file" in request.FILES.keys()):
        Productions.objects.create(
            name=request.POST["name"],
            category_id=int(request.POST["category_id"]),
            price=float(request.POST["price"]),
            description=request.POST["description"],
            Image=request.FILES["file"]
        )
        return JsonResponse(assemble_success_msg("success"))

    else:
        return JsonResponse(assemble_fail_msg("lack of parameters"))


def production_delete(request):
    '''
    delete a production
    :param request: parameter: production id
    :return:
    '''

    if request.method != "POST":
        return JsonResponse(assemble_fail_msg("error request method"))

    if "id" in request.POST.keys():
        Productions.objects.get(id=request.POST["id"]).delete()
        return JsonResponse(assemble_success_msg("success delete"))

    else:
        return JsonResponse(assemble_fail_msg("lack or wrong parameters"))


def production_update(request):
    '''
    add a production
    :param request: parameter: id(production), name, category_id, price, description, Image
    :return: msg
    @tested
    '''

    if request.method != "POST":
        return JsonResponse(assemble_fail_msg("error request method"))

    if (
            ("id" in request.POST.keys())
            and "name" in request.POST.keys()) \
            and ("category_id" in request.POST.keys()) \
            and ("price" in request.POST.keys()) \
            and ("description" in request.POST.keys()) \
            and ("file" in request.FILES.keys()):

        production = Productions.objects.get(id=request.POST["id"])
        production.name = request.POST["name"]
        production.category_id = int(request.POST["category_id"])
        production.price = float(request.POST["price"])
        production.description = request.POST["description"]
        production.file = request.FILES["file"]
        production.save()
        return JsonResponse(assemble_success_msg("success"))

    else:
        return JsonResponse(assemble_fail_msg("lack of parameters"))
