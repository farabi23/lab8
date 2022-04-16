from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import Product, Category


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(product.to_json())

def category_show(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request, categ_id):
    try:
        categ = Category.objects.get(id=categ_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(categ.to_json())

def categ_id(request, cat_id):

    cat = Product.objects.all().filter(cat=cat_id)
    cat_json = [category.to_json() for category in cat]
    return JsonResponse(cat_json, safe=False)



'''
categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)
'''


