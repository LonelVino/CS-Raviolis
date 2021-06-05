# Create your views here.
from django.http import JsonResponse
from api_v1.order.models import UserOrder
from api_v1.order.models import OrderItem

import json

def one_order_item(request):
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            ord_itm_1= OrderItem.objects.filter(id=id)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        #TODO: write this as a map function
        info =  {'id': ord_itm_1.id, 'itm_price': ord_itm_1.itm_price, 'gotten': ord_itm_1.gotten,
        'quantity': ord_itm_1.quantity, 'product_id': ord_itm_1.product_id, 'order_id': ord_itm_1.order_id}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'order_item_info': info
            }
        })

#TODO: change select according to slug to according to the name
def user_one_order(request):   # Select the product according to the id and slug
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            ord_1= UserOrder.objects.filter(id=id)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        #TODO: write this as a map function
        info =  {'id': ord_1.id, 'username': ord_1.username, 'user_id': ord_1.user_id, 
        'usr_price': ord_1.usr_price,'gotten': ord_1.gotten,
        'paid': ord_1.paid, 'created': ord_1.created, 'updated': ord_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'order_info': info
            }
        })

def user_one_order_items(request):   # Select the product according to the id and slug
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            ord_1= UserOrder.objects.filter(id=id)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        one_ord_items = list(OrderItem.objects.filter(order_id = ord_1.id).values())
        if len(one_ord_items) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all orders successfully',
                'data': {
                    'total': len(one_ord_items),
                    'order_items_info': one_ord_items
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})


def user_all_orders(request):
     if request.method == 'GET':
        usr_id = request.GET.get('usr_id', default=0)
        if usr_id != 0:
            all_orders = list(UserOrder.objects.filter(user_id=usr_id).values())
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        orders = []
        for i in all_orders:
            orders.append(i)
        if len(all_orders) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all orders successfully',
                'data': {
                    'total': len(orders),
                    'order_infos': orders
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def check_user_one_item(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        # print('REC=================:', rec['id'], rec['gotten'])
        user_order_1 = OrderItem.objects.get(id = rec['id'])
        user_order_1.gotten = rec['gotten']
        print(user_order_1.gotten)
        user_order_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
        })
    else: 
        return JsonResponse({
            'code': 500,
            'msg': 'Update Failed, incorrect request method!'
        })

def check_user_all_items(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        user_order_1 = UserOrder.objects.filter(user_id = rec['user_id'])
        user_order_1.gotten = rec['gotten']
        user_order_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
        })
    else: 
        return JsonResponse({
            'code': 500,
            'msg': 'Update Failed, incorrect request method!'
        })

def add_order_item(request):
    pass

def del_user_one_item(request):
    pass

def delete_user_one_order(request):
    pass

def delete_user_all_orders(request):
    pass




'''===================== ADMIN PART ====================='''
def all_users_orders(request):
    if request.method == 'GET':
        orders = []
        all_orders = list(UserOrder.objects.all())
        for i in all_orders:
            tmp = {}
            tmp['id'] = i.id
            tmp['username'] = i.username
            tmp['usr_price'] = i.usr_price
            tmp['paid'] = i.paid
            tmp['created'] = i.created
            tmp['updated'] = i.updated
            orders.append(tmp)
        if len(all_orders) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all orders successfully',
                'data': {
                    'total': len(orders),
                    'order_infos': orders
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def order_items(request):
    all_order_items = list(OrderItem.objects.all())
    order_items = []
    for i in all_order_items:
        tmp = {}
        tmp['id'] = i.id
        tmp['itm_price'] = i.itm_price
        tmp['quantity'] = i.quantity
        tmp['order_id'] = i.order_id
        tmp['product_id'] = i.product_id
        order_items.append(tmp)
    if len(all_order_items) >= 0:
        return JsonResponse({
            'code': 200,
            'msg': 'get all order items successfully',
            'data': {
                'total': len(order_items),
                'order_itms_infos': order_items
            }
        })
    else:
        return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def update_order_item(request):
    pass
