from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

# fuction products
def list_products(request):
    return render(request,'products.html')

# fuction for single product
def detail_product(request):
    return render(request,"product_detail.html")