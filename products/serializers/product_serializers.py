from rest_framework import serializers

from products.models.product_models import Product
from products.serializers.user_serializers import UserSerializer
from products.utils.constants import PRODUCT_BUYERS_AMOUNT_VALIDATION_ERROR_MESSAGE


class CreateOrUpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['buyers', 'name', 'price', 'description', 'amount']

    def create(self, validated_data):
        """
        Set user_owner as authenticated user on Product create
        """
        validated_data['user_owner'] = self.context['request'].user
        return Product.objects.create(**validated_data)

    def validate(self, data):
        """
        Validate if number of buyers is less or equal to amount of Products
        """
        if data.get('buyers') and len(data['buyers']) > data['amount']:
            raise serializers.ValidationError(PRODUCT_BUYERS_AMOUNT_VALIDATION_ERROR_MESSAGE)
        return data


class ProductSerializer(serializers.ModelSerializer):
    user_owner = UserSerializer()
    buyers = UserSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
