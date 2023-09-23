from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from products.models.user_models import CustomUser
from products.utils.constants import USER_PIN_VALIDATION_ERROR_MESSAGE, \
    USER_CARD_NUMBER_VALIDATION_ERROR_MESSAGE


class CreateOrUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password', 'username', 'email', 'card_number', 'pin_code']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return CustomUser.objects.create(**validated_data)

    @staticmethod
    def __validate_pin(pin_str):
        """
        Validate pin is numeric and is 4 digits
        """
        if not (pin_str.isnumeric() and len(pin_str) == 4):
            raise serializers.ValidationError(USER_PIN_VALIDATION_ERROR_MESSAGE)

    @staticmethod
    def __validate_card_number(card_number_str):
        """
        Validate card_number is numeric and is 16 digits
        """
        if not (card_number_str.isnumeric() and len(card_number_str) == 16):
            raise serializers.ValidationError(USER_CARD_NUMBER_VALIDATION_ERROR_MESSAGE)

    def validate(self, attrs):
        self.__validate_pin(attrs['pin_code'])
        self.__validate_card_number(attrs['card_number'])
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'card_number', 'pin_code', 'is_superuser']
