from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class ProductReviews(models.Model):
    """ model for product reviews """

    title = models.CharField(max_length=200, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_added", null=True)
       
    class Meta:
        """
        will order class based on crrated on date.
        inspired by code institue blog walk through project
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        django docs recomends to define this method
        """
        return f"Comment {self.body} by {self.title}"    
    
