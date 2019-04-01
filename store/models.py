from django.db import models
from django.conf import settings
from django.utils import timezone

class Product(models.Model):
	id = models.CharField(primary_key = True, max_length = 20)
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.FloatField()
	image = models.CharField(max_length=200, null=True)

	def saveProduct(self):
		self.save()

	def __str__(self):
		return self.name




class Order(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	recipient = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	creditCard = models.IntegerField()
	order_date = models.DateTimeField(blank=True, null=True)

	def saveOrder(self):
		self.order_date = timezone.now()
		self.save()

	def __str__(self):
		return self.recipient
