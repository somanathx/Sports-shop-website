from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,"index.html")

# fuction for return product list page
def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list = Products.objects.all()
    product_paginator=Paginator(product_list,40)
    product_list=product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request,'products.html',context)

# fuction for single product
def detail_product(request):
    return render(request,"product_detail.html")