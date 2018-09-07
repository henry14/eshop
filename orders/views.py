from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from paypal.standard.forms import PayPalPaymentsForm
from decimal import Decimal
import uuid

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(
			            order=order,
				    product=item['product'],
				    price=item['price'],
				    quantity=item['quantity']
				)
			cart.clear()
			
			#order_created.delay(order.id)
			
			request.session['order_id'] = order.id
			
			return redirect(reverse('payment:process'))
			
			#return render(request, 'orders/created.html', {'order': order})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/create.html', {'form': form})


def view_that_asks_for_money(request):
	cart = Cart(request)
	paypal_dict = {
	    "business": "henrytebs@inceptionz.com",
	    "invoice": str(uuid.uuid1()),
	    "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
	    "return": request.build_absolute_uri(reverse('estore/list.html')),
	    "cancel_return": request.build_absolute_uri(reverse('/')),
	}	

	for index in range(len(cart)):
		itemname = item_name_ + str(index +1)
		amount = amount_ + str(index +1)
		paypal_dict[itemname] = cart[index]['product']
		paypaypal_dict[amount] = Decimal(cart[index]['price']) * cart[index]['quantity']

	form = PayPalPaymentsForm(initial=paypal_dict)
	context = {"form": form}
	return render(request, "payment.html", context)

