from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Order
from .forms import OrderForm, addForm

def index(request):
	products = Product.objects.all()
	return render(request, 'store/index.html', {'products': products})
	
def productPage(request, pk):
	product = get_object_or_404(Product, id=pk)
	return render(request, 'store/productPage.html', {'product': product})
	
def orderPage(request, pk):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.product = get_object_or_404(Product, id=pk)
			order.saveOrder()
			return redirect('product', pk=pk)
	else:
		form = OrderForm()
	return render(request, 'store/orderPage.html', {'form': form})

def addProductPage(request):
	if request.method == "POST":
		form = addForm(request.POST)
		if form.is_valid():
			product = form.save(commit = False)
			product.saveProduct()
			pk = product.id
			return redirect('product', pk=pk)
	else:
		form = addForm()
	return render(request, 'store/addProductPage.html', {'form': form})
	
def fulfillmentPage(request):
	orders = Order.objects.all()
	return render(request, 'store/fulfillmentPage.html', {'orders': orders})
