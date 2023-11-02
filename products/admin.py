from django.contrib import admin
from .models import Product, CatgoryProduct, Comments, Basket, DeliveriInformation

# Register your models here.

class CustomProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_added']


class CustomProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CustomCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


class CustomBasketAdmin(admin.ModelAdmin):
    list_display = ['user_for_basket']
    readonly_fields = ('update_total_price',)

class CustomDeliveryAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id', 'basket']


admin.site.register(Product, CustomProductAdmin)
admin.site.register(CatgoryProduct, CustomProductCategoryAdmin)
admin.site.register(Comments, CustomCommentsAdmin)
admin.site.register(Basket, CustomBasketAdmin)
admin.site.register(DeliveriInformation, CustomDeliveryAdmin)


