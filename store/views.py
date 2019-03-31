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
	if request.user.is_authenticated:
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
	else:
		return redirect('index');

def fulfillmentPage(request):
	if request.user.is_authenticated:
		orders = Order.objects.all()
		return render(request, 'store/fulfillmentPage.html', {'orders': orders})
	else:
		return redirect('index');

def removeOrder(request, pk):
	if request.user.is_authenticated:
		Order.objects.filter(pk=pk).delete()
		return render(request, 'store/removePage.html')
	else:
		return redirect('index');
		

def editProductPage(request, pk):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = addForm(request.POST)
			product = get_object_or_404(Product, id = pk)
			product.delete()
			if form.is_valid():
				product = form.save(commit = False)
				product.saveProduct()
				pk = product.id
				return redirect('product', pk=pk)
		else:
			product = get_object_or_404(Product, id = pk)
			form = addForm()
			form.initial['id'] = pk
			form.initial['name'] = product.name
			form.initial['description'] = product.description
			form.initial['price'] = product.price

		return render(request, 'store/editProductPage.html', {'form': form})
	else:
		return redirect('index');
