from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category', 'stripe_product_price')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)

    def save(self):
        if not self['stripe_product_price']:
            self.create_stripe_product_price()
        super(ProductAdmin, self).save()


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0
