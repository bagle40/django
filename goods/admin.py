from django.contrib import admin

from goods.models import Categories,Products

#admin.site.register(Categories)

#admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','category','quantity','price']
    list_editable=['price','quantity']
    search_fields=['name']
    list_filter=['price','category']

