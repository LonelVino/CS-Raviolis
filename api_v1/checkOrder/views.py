# Create your views here.
from django.http import JsonResponse
from api_v1.checkOrder.models import checkOrder
from api_v1.checkOrder.models import checkTag
import json

def one_tag(request):
    if request.method == 'GET':
        id = request.GET.get('id',default=0)
        if id != 0:
            check_tag_1 = checkTag.objects.filter(id=id)[0]
        else:
           return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     

        info = {'id': check_tag_1.id, 'name': check_tag_1.name, 
        'created_time': check_tag_1.created, 'end_time': check_tag_1.ended}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'info': info
            }
        })

def all_tags(request):
    if request.method == 'GET':
        all_check_tags = list(checkTag.objects.all().values()) 
        print(all_check_tags)
        return JsonResponse({
            'code': 200,
            'msg': 'get all information successfully',
            'data': {
                'total': len(all_check_tags),
                'infos': all_check_tags
            }
        })

def one_order(request):
    if request.method == 'GET':
        id = request.GET.get('id',default=0)
        slug = request.GET.get('slug',default='')
        if id != 0:
            check_order_1 = checkOrder.objects.filter(id=id)[0]
        elif slug != '':
            check_order_1 = checkOrder.objects.filter(slug=slug)[0]
        else:
           return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     

        info = {'id': check_order_1.id, 'gotten': check_order_1.gotten,
        'itm_price': check_order_1.itm_price, 'product_id': check_order_1.product_id,
        'quantity': check_order_1.quantity, 'tag_id': check_order_1.tag_id,
        'product_name': check_order_1.product_name, 'category_name': check_order_1.category_name}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'info': info
            }
        })

def all_orders(request):
    if request.method == 'GET':
        tag_id = request.GET.get('tag_id',default=0)
        if tag_id != 0:
            all_check_orders = list(checkOrder.objects.filter(tag_id=tag_id).values())
            return JsonResponse({
                'code': 200,
                'msg': 'get all information successfully',
                'data': {
                    'total': len(all_check_orders),
                    'infos': all_check_orders
                }
            })
        else:
            return JsonResponse({
                'code': 3005,
                'msg': 'Parameters does not meet the requirements!'
            })     

def check_one_order(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        # print('REC=================:', rec['id'], rec['gotten'])
        check_order_1 = checkOrder.objects.get(id = rec['id'])
        check_order_1.gotten = rec['gotten']
        check_order_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
        })
    else: 
        return JsonResponse({
            'code': 500,
            'msg': 'Update Failed, incorrect request method!'
        })

def add_order_quantity(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        # print('REC=================:', rec['id'], rec['gotten'])
        check_order_1 = checkOrder.objects.get(id = rec['id'])
        check_order_1.quantity = rec['quantity']
        check_order_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
        })
    else: 
        return JsonResponse({
            'code': 500,
            'msg': 'Update Failed, incorrect request method!'
        })

def add_tag(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        tag_1 = checkTag(name=rec['name'], created=rec['created'], ended=rec['ended'])
        tag_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add User Successfully!',
            'data':{
                'created_time': rec['created']
            }
        })


def add_order(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        order_1 = checkOrder(tag_id=rec['tag_id'], product_id=rec['product_id'], 
        itm_price = rec['itm_price'], quantity=rec['quantity'], gotten=rec['gotten'],
        product_name =rec['product_name'], category_name = rec['category_name'])
        order_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Order Successfully!',
            'data':{
                'name': rec['name']
            }
        })

def update_tag(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        tag_1 = checkTag.objects.get(id = rec['id'])
        tag_1.name=rec['name']; tag_1.created=rec['created']; tag_1.ended=rec['ended']; 
        tag_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
            'data':{
                'name': rec['name']
            }
        })
    

def update_order(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        order_1 = checkOrder.objects.get(id = rec['id'])

        order_1.tag_id=rec['tag_id']; order_1.product_id=rec['product_id']; 
        order_1.itm_price = rec['itm_price']; order_1.quantity=rec['quantity']; order_1.gotten=rec['gotten'];
        order_1.product_name =rec['product_name']; order_1.category_name = rec['category_name']
        order_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
            'data':{
                'name': rec['name']
            }
        })

def delete_one_tag(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        tag_1 = checkTag.objects.get(id = id)
        order_items = checkOrder.objects.filter(tag_id = tag_1.id)
        for item in order_items:
            item.delete()
        tag_1.delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })

def delete_one_order(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        order_1 = checkOrder.objects.get(id = id)
        order_1.delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })

def delete_all_orders(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        order_items = checkOrder.objects.filter(tag_id = id)
        for item in order_items:
            item.delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })

