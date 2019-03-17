from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Order

def index(request):
	products = Product.objects.all()
	return render(request, 'store/index.html', {'products': products})
	
def productPage(request, pk):
	product = get_object_or_404(Product, id=pk)
	return render(request, 'store/productPage.html', {'product': product})


