from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'store/index.html')
	
def productPage(request, pk):
	return render(request, 'store/productPage.html')


