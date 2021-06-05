# Create your views here.
from django.http import JsonResponse
from api_v1.order.models import UserOrder
from api_v1.order.models import OrderItem

#TODO: change select according to slug to according to the name
def one_order(request):   # Select the product according to the id and slug
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
        info =  {'id': ord_1.id, 'username': ord_1.username, 'usr_price': ord_1.usr_price,
        'paid': ord_1.paid, 'created': ord_1.created, 'updated': ord_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'ord_info': info
            }
        })

def orders(request):
     if request.method == 'GET':
        all_orders = list(UserOrder.objects.all())
        orders = []
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

def one_order_item(request):   # Select the product according to the id and slug
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        slug = request.GET.get('slug', default='')
        if id != 0:
            ord_itm_1= OrderItem.objects.filter(id=id)[0]
        elif slug == '':
            ord_itm_1 = OrderItem.objects.filter(slug=slug)[0]
        else:
            return JsonResponse({
                'code': 3005,
                'msg': 'Parameters does not meet the requirements!'
            })     
        #TODO: write this as a map function
        info =  {'id': ord_itm_1.id, 'itm_price': ord_itm_1.itm_price, 'quantity': ord_itm_1.quantity,
        'product_id': ord_itm_1.product_id, 'order_id': ord_itm_1.order_id}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information of order item successfully',
            'data': {
                'ord_itm_info': info
            }
        })

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



def add_order(request):
    pass

def add_order_item(request):
    pass

def update_order(request):
    pass

def update_order_item(request):
    pass

def del_order(request):
    pass


def del_order_item(request):
    pass