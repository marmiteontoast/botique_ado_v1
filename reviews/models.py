from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Product_reviews(models.Model):
    """ model for product reviews """

    title = models.CharField(max_length=200, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_added", null=True)
       
        
        
