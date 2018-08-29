from django.shortcuts import render
from django.db.models import Sum 
from estore.models import Product
from orders.models import OrderItem
from django.db.models.functions import Coalesce

app_name = "charts"

def chart_data(request):
	product_dataset = Product.objects.values('name','stock') \
	    .annotate(stock_sum=Sum('stock')).order_by('name')

	item_dataset = OrderItem.objects.values('product__name','quantity') \
	    .annotate(item_sum=Coalesce(Sum('quantity'), 0)).order_by('product__name')

	return render(request, 'charts/graph.html',{'item_dataset':item_dataset, 'product_dataset':product_dataset})

