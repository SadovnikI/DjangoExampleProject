import uuid as uuid
from django.db import models
from django.utils.text import slugify
from rest_framework import serializers

from products.models.user_models import CustomUser
from products.utils.constants import PRODUCT_BUYERS_AMOUNT_VALIDATION_ERROR_MESSAGE


class Product(models.Model):
    """
    Model for Products created by user
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=240, unique=True)
    slag = models.SlugField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    amount = models.PositiveIntegerField()

    user_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_owner')
    buyers = models.ManyToManyField(CustomUser, related_name='buyers', blank=True)

    def clean(self):
        """
        Check if number of buyers is less or equal to amount of Products before save to DB
        """
        if self.pk:
            if self.buyers.count() > self.amount:
                raise serializers.ValidationError(PRODUCT_BUYERS_AMOUNT_VALIDATION_ERROR_MESSAGE)

    def save(self, *args, **kwargs):
        """
        Update slug from name before save
        """
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
