from django.contrib import admin
from .models import ProductReviews


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'created_on',
        'posted_by',
        'product'
    )


admin.site.register(ProductReviews)

# Register your models here.
