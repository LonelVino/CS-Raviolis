# Create your views here.
import json
from django.http import JsonResponse
from .models import CartItem
from .models import Cart

#TODO: change select according to slug to according to the name
def one_cart(request):   # Select the product according to the id and slug
    if request.method == 'GET':
        usr_id = request.GET.get('usr_id', default=0)
        print('user_id: ================', usr_id)
        if usr_id != 0:
            cart_1 = Cart.objects.filter(user_id=usr_id)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        #TODO: write this as a map function
        info =  {'id': cart_1.id, 'usr_id': cart_1.user_id, 'ttl_price': cart_1.ttl_price,
        'created': cart_1.created, 'updated': cart_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get your cart successfully',
            'data': {
                'cart_info': info
            }
        })


def carts(request):
    if request.method == 'GET':
        all_carts = list(Cart.objects.all())
        carts = []
        for i in all_carts:
            tmp = {}
            tmp['id'] = i.id
            tmp['usr_id'] = i.user_id
            tmp['ttl_price'] = i.ttl_price
            tmp['created'] = i.created
            tmp['updated'] = i.updated
            carts.append(tmp)
        if len(all_carts) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all carts successfully',
                'data': {
                    'total': len(carts),
                    'cart_infos': carts
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

# def one_cart_item(request):   # Select the product according to the id and slug
#     if request.method == 'GET':
#         id = request.GET.get('id', default=0)
#         print('id: ================', id)
#         if id != 0:
#             cart_item_1 = CartItem.objects.filter(id=id)[0]
#         else:
#             return JsonResponse({
#                 'code': 3005,
#                 'msg': 'Parameters does not meet the requirements!'
#             })     
#         #TODO: write this as a map function
#         info =  {'id': cart_item_1.id, 'itm_price': cart_item_1.itm_price, 'quantity': cart_item_1.quantity,
#         'product_id': cart_item_1.product_id, 'card_id': cart_item_1.order_id}
#         return JsonResponse({
#             'code': 200,
#             'msg': 'Get information of cart item successfully',
#             'data': {
#                 'cart_itm_info': info
#             }
#         })


def cart_items(request):
    all_cart_items = list(CartItem.objects.all())
    cart_items = []
    for i in all_cart_items:
        print('CartItem.attr---------------------------: ', i.__dict__)
        tmp = {}
        tmp['id'] = i.id
        tmp['itm_price'] = i.itm_price
        tmp['quantity'] = i.quantity
        tmp['cart_id'] = i.cart_id
        tmp['product_id'] = i.product_id
        cart_items.append(tmp)
    if len(all_cart_items) >= 0:
        return JsonResponse({
            'code': 200,
            'msg': 'get all cart items successfully',
            'data': {
                'total': len(cart_items),
                'cart_itms_infos': cart_items
            }
        })
    else:
        return JsonResponse({'code': 200, 'msg': 'Empty table!'})


def add_cart(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cart_1 = Cart(username=rec['username'], ttl_price=rec['ttl_price'])
        cart_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'username': rec['username']
            }
        })

def add_cart_item(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cart_item_1 = CartItem(itm_price=rec['itm_price'], quantity=rec['quantity'],
        order_id=rec['order_id'], product_id=rec['product_id'])
        cart_item_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'product_id': rec['product_id']
            }
        })  


def update_cart_item(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cart_item_1 = CartItem.objects.get(id = rec['id'])
        cart_item_1.quantity = rec['quantity']
        cart_item_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
        })
    else: 
        return JsonResponse({
            'code': 500,
            'msg': 'Update Failed, incorrect request method!'
        })

def del_cart(request):
    # remove all the cart items
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        cart_items = CartItem.objects.filter(cart_id = id)
        print(cart_items)
        # Cart.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
            'cart_items': cart_items
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })

def del_cart_item(request):
    # remove one cart item in the cart
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        CartItem.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })
