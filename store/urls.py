from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('product/<int:pk>/', views.productPage, name='product'),
	path('order/<int:pk>/', views.orderPage, name='order'),
	path('add/', views.addProductPage, name='add'),
	path('fulfillment', views.fulfillmentPage, name='fulfillment'),
	path('removeOrder/<int:pk>/', views.removeOrder, name='remove'),
    path('edit/<int:pk>/', views.editProductPage, name='edit'),
	path('confirmation/<int:pk>/', views.ConfirmationPage, name='confirmation'),
	#path('management', views.managementPage),
	#path('orders', view.ordersPage),
]
