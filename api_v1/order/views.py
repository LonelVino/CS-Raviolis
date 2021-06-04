from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from api_v1.shop.models import Product 
from api_v1.shop.models import Category


# Create your views here.
#TODO: change select according to slug to according to the name
def one_order(request):   # Select the product according to the id and slug
    pass

def orders(request):
    pass


def add_order(request):
    pass


def update_order(request):
    pass


def del_order(request):
    pass

