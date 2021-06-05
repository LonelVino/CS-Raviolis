import json
from django.http import JsonResponse
from api_v1.shop.models import Product 
from api_v1.shop.models import Category


# Create your views here.
#TODO: change select according to slug to according to the name
def one_product(request):   # Select the product according to the id and slug
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        slug = request.GET.get('slug', default='')
        if id != 0:
            prod_1= Product.objects.filter(id=id)[0]
        elif slug == '':
            prod_1 = Product.objects.filter(slug=slug)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        newImage = json.dumps(str(prod_1.image)) 
        #TODO: write this as a map function
        info =  {'id': prod_1.id, 'name': prod_1.name, 'category_id': prod_1.category_id,
        'slug': prod_1.slug, 'image': newImage, 'quantity_unit': prod_1.quantity_unit, 
        'description': prod_1.description, 'price': prod_1.price, 'dt_info': prod_1.dt_info,
        'created': prod_1.created, 'updated': prod_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'prod_info': info
            }
        })

def products(request):
    if request.method == 'GET':
        all_products = list(Product.objects.all())
        products = []
        for i in all_products:
            tmp = {}
            tmp['id'] = i.id
            tmp['name'] = i.name
            tmp['slug'] = i.slug
            tmp['category_id'] = i.category_id
            tmp['quantity_unit'] = i.quantity_unit
            tmp['description'] = i.description
            tmp['price'] = i.price
            tmp['dt_info'] = i.dt_info
            tmp['created'] = i.created
            tmp['updated'] = i.updated
            newImage = json.dumps(str(i.image)) 
            tmp['image'] = newImage

            products.append(tmp)
        if len(all_products) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all products successfully',
                'data': {
                    'total': len(products),
                    'prod_infos': products
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def one_category(request):  # Select the product according to the slug
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        slug = request.GET.get('slug', default='')
        if id != 0:
            cat_1 = Category.objects.filter(id=id)[0]
        elif slug == '':
            cat_1 = Category.objects.filter(slug=slug)[0]
        else:
            return JsonResponse({
                'code': 3005,
                'msg': 'Parameters does not meet the requirements!'
            })     

        #TODO: write this as a map function
        info =  {'id': cat_1.id, 'name': cat_1.name, 'slug': cat_1.slug,}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information of category successfully',
            'data': {
                'cat_info': info
            }
        })

def categories(request):
    if request.method == 'GET':
        all_categories = list(Category.objects.all())
        categories = []
        for i in all_categories:
            tmp = {}
            tmp['id'] = i.id
            tmp['name'] = i.name
            tmp['slug'] = i.slug
            categories.append(tmp)
        if len(all_categories) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all products successfully',
                'data': {
                    'total': len(categories),
                    'cat_infos': categories
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def add_cat(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cat_1 = Category(name=rec['name'], slug=rec['slug'], )
        cat_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })

keys = ['category' , 'image', 'quantity_unit' , 'description' , 'price' , 'dt_info' 
            'created' , 'updated' ]
def add_prod(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cat_1 = Product(name=rec['name'], slug=rec['slug'], category=rec['category'], 
            image=rec['image'], quantity_unit= rec['quantity_unit'], price = rec['price'],
            dt_info = rec['dt_info'], created=rec['created'], updated=rec['updated'])
        cat_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })


def update_cat(request):
    pass

def update_prod(request):
    pass

def del_cat(request):
    pass

def del_prod(request):
    pass