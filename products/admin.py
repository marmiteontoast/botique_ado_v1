from django.contrib import admin
from .models import Product, Category, Comment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'product', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')


class WishlistAdmin(admin.ModelAdmin):

    list_display = ('product', 'created_on')
    list_filter = ('created_on',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)