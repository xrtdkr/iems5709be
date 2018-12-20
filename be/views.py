# coding: utf-8
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from be.models import *
from utils import *
import json
from ierg4210Be import settings
from tools import *
import re
import time
from alipay import AliPay


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
        ret.append({"id": category.id, "name": category.name, "description": category.description})
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


def register(request):
    if request.method != 'POST':
        return JsonResponse(assemble_fail_msg("error request method"))

    body_data = json.loads(request.body)

    if "username" and "password" and "email" in body_data.keys():
        username = body_data["username"]
        email = body_data["email"]
        password = body_data["password"]

        regex_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        match_group = re.match(regex_pattern, email)

        if not match_group:
            return JsonResponse(assemble_fail_msg("email format is incorrect"))

        if len(password) < 8:
            return JsonResponse(assemble_fail_msg("password is not secure"))

        if len(username) > 80:
            return JsonResponse(assemble_fail_msg("username is too long"))
        password_hashed = password_hash(password)
        User.objects.create(email=email, nickname=username, password=password_hashed)
        return JsonResponse(assemble_success_msg("register success, please login"))
    else:
        return JsonResponse(assemble_fail_msg("post data parameter error"))


def login(request):
    if request.method != 'POST':
        return JsonResponse(assemble_fail_msg("error request method"))

    body_data = json.loads(request.body)

    if "email" and "password" in body_data.keys():
        email = body_data["email"]
        password = body_data["password"]

        user_l = User.objects.filter(email=email)

        if len(user_l) == 0:
            return JsonResponse(assemble_fail_msg("username or password error"))
        user = user_l[0]
        password_hashed = user.password
        if password_verify(password, password_hashed):
            res = JsonResponse(assemble_success_msg("login success"))
            session = password_hash(str(time.time()) + user.nickname)
            user.session_id = session
            user.save()
            res.set_cookie("user", session)
            print res.__dict__
            return res
        else:
            return JsonResponse(assemble_fail_msg("username or password error"))
    else:
        return JsonResponse(assemble_fail_msg("post data parameter error"))


def logout(request):
    if 'user' not in request.COOKIES.keys():
        pass
    else:
        del request.COOKIES['user']
    return JsonResponse(assemble_success_msg("success"))  # 要在服务器端进行修改


def change_password(request):
    '''
    :param request:  {"new_password": "xxx", "old_password": "xxx"}
    :return:
    '''
    if 'user' not in request.COOKIES.keys():
        return JsonResponse(assemble_fail_msg(data="please login"))

    body_data = request.POST
    session_id = request.COOKIES['user']

    if 'old_password' and 'new_password' in body_data.keys():
        old_password = body_data['old_password']
        new_password = body_data['new_password']
        user = User.objects.get(session_id=session_id)
        if password_verify(old_password, user.password):
            user.password = password_hash(new_password)
            user.save()
            return JsonResponse(assemble_success_msg("success"))
        else:
            return JsonResponse(assemble_fail_msg("old password is not correct"))
    else:
        return JsonResponse(assemble_fail_msg("post data parameter error"))


def get_cart(request):
    '''
    :param request: None
    :return:
    {
        "msg": "success",
        "data": [1,2,3,4],
    }
    '''

    if 'user' not in request.COOKIES.keys():
        return JsonResponse(assemble_fail_msg(data="please login"))

    user_session = request.COOKIES['user']
    user = User.objects.get(session_id=user_session)

    if len(ShoppingCart.objects.filter(user_id=user.id)) == 0:
        return JsonResponse(
            assemble_success_msg([])
        )
    else:
        shopping_cart = ShoppingCart.objects.get(user_id=user.id)

    shopping_cart_id = shopping_cart.id
    prod_set = ProductionInShoppingCart.objects.filter(shopping_cart_id=shopping_cart_id)
    pid_list = []
    for prod in prod_set:
        pid_list.append(prod.production_id)

    ret_data = []
    for pid in pid_list:
        print pid
        ret_data.append(Productions.objects.get(id=pid).get_production())
    return JsonResponse(
        assemble_success_msg(ret_data)
    )


def add_prod_cart(request):
    '''
    :param request: {"pid": xxx}
    :return:
    '''
    if request.method != 'POST':
        return JsonResponse(assemble_fail_msg("error request method"))
    pid = request.POST.get('pid')
    pid = int(pid)
    if 'user' not in request.COOKIES.keys():
        return JsonResponse(assemble_fail_msg(data="please login"))

    user_session = request.COOKIES['user']
    user = User.objects.get(session_id=user_session)

    if len(ShoppingCart.objects.filter(user_id=user.id)) == 0:
        shopping_cart = ShoppingCart.objects.create(
            user_id=user.id
        )
    else:
        shopping_cart = ShoppingCart.objects.get(user_id=user.id)

    ProductionInShoppingCart.objects.create(production_id=pid, shopping_cart_id=shopping_cart.id)
    return JsonResponse(assemble_success_msg("success"))


def delete_prod_cart(request):
    '''
    :param request: {"pid": xxx}
    :return:
    '''
    if request.method != 'POST':
        return JsonResponse(assemble_fail_msg("error request method"))

    pid = int(request.POST.get('pid'))

    if 'user' not in request.COOKIES.keys():
        return JsonResponse(assemble_fail_msg(data="please login"))

    user_session = request.COOKIES['user']
    user = User.objects.get(session_id=user_session)

    if len(ShoppingCart.objects.filter(user_id=user.id)) == 0:
        return JsonResponse(assemble_fail_msg("user have no shopping cart"))
    else:
        shopping_cart = ShoppingCart.objects.get(user_id=user.id)

    ProductionInShoppingCart.objects.filter(production_id=pid, shopping_cart_id=shopping_cart.id)[0].delete()
    return JsonResponse(assemble_success_msg("success"))


def checkout(request):
    '''

    :param request:
    :return:
    '''

    if 'user' not in request.COOKIES.keys():
        return JsonResponse(assemble_fail_msg(data="please login"))

    user_session = request.COOKIES['user']

    user = User.objects.get(session_id=user_session)

    if len(ShoppingCart.objects.filter(user_id=user.id)) == 0:
        return JsonResponse(assemble_fail_msg("user have no shopping cart"))

    shopping_cart = ShoppingCart.objects.get(user_id=user.id)
    prod_set = ProductionInShoppingCart.objects.filter(shopping_cart_id=shopping_cart.id)
    if len(prod_set) == 0:
        return JsonResponse(assemble_fail_msg("empty"))
    ret_data = []
    bill = Bill.objects.create(
        series=yield_series(),
        create_time=TimeHandle.get_time_now_string(),
        state=1,
        user_id=user.id
    )

    sum = 0
    for prod in prod_set:
        _data = Productions.objects.get(id=prod.production_id).get_production()
        sum = sum + float(_data['price'])
        ret_data.append(_data)
        ProductionInBill.objects.create(bill_id=bill.id, production_id=prod.id)
    shopping_cart.delete()
    shopping_cart.save()

    alipay_public_key_string = open("be/key/app_public_key.pem").read()
    app_private_key_string = open("be/key/app_private_key.pem").read()

    alipay = AliPay(
        appid="2016092300576596",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA",
        debug=False,
    )

    subject = u"测试订单".encode("utf8")

    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="20161112",
        subject=subject,
        total_amount=sum,
        return_url="http://s13.ierg4210.ie.cuhk.edu.hk",
        notify_url="http://s13.ierg4210.ie.cuhk.edu.hk"  # 可选, 不填则使用默认notify url
    )

    data = dict()
    data['bill'] = bill.get_bill()
    data['prod'] = ret_data
    data['alipay'] = "https://openapi.alipaydev.com/gateway.do?" + order_string

    return JsonResponse(assemble_success_msg(data=data))

# Create your views here.
