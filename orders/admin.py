from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']

	inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
