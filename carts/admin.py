from django.contrib import admin

# Register your models here.
from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestap"
    search_fields ="product", "quantity", "created_timestap"
    readonly_fields = ("created_timestap",)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user','product_display','quantity','created_timestap']
    list_filter=['created_timestap','user','product__name']

    
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    
    def product_display(self, obj):
        return str(obj.product.name)
        

