from django.contrib import admin
from .models import Item, Announcement, Preorder, Order, OrderUpdate

# Register your models here.

class ItemSearch(admin.ModelAdmin):
    search_fields = ["Title", "Category"]

admin.site.register(Item, ItemSearch)
# admin.site.register(Announcement)
# admin.site.register(CartItem)
admin.site.register(Preorder)
admin.site.register(Order)
admin.site.register(OrderUpdate)

admin.site.site_title = "CircuitBunny | Admin"
admin.site.site_header = "Admin Panel"