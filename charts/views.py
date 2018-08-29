from django.shortcuts import render
from django.db.models import Sum 
from estore.models import Product

app_name = "charts"

def chart_data(request):
	dataset = Product.objects.values('name','stock').annotate(stock_count=Sum('stock')).order_by('stock')
	return render(request, 'charts/graph.html', {'dataset':dataset})

