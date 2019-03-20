from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('product/<int:pk>/', views.productPage, name='product'),
	path('order/<int:pk>/', views.orderPage, name='order'),
	#path('confirmation', views.confirmationPage),
	#path('Management', views.managementPage),
	#path('orders', view.ordersPage),
]
