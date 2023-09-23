from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from products.models import CustomUser
from products.models.product_models import Product


class Command(BaseCommand):
    help = "Populates DB with Products and CustomUsers"

    def handle(self, *args, **options):
        u1 = CustomUser.objects.create(**{
                        "uuid": 'ca81d72f-0138-4d05-9382-310795c07259',
                        "password": make_password('password1'),
                        "username": "Username1",
                        "email": "user1@example.com",
                        "card_number": "1111111111111111",
                        "pin_code": "1111"
                    })
        u2 = CustomUser.objects.create(**{
                        "uuid": '59dc64e5-645a-4375-87b3-f59f795fd15a',
                        "password": make_password('password2'),
                        "username": "Username2",
                        "email": "user2@example.com",
                        "card_number": "1111111111111112",
                        "pin_code": "1112"
                    })
        u3 = CustomUser.objects.create(**{
                        "uuid": '5f8fb6c7-bc96-408e-9ac6-c1ecc468af57',
                        "password": make_password('password3'),
                        "username": "Username3",
                        "email": "user3@example.com",
                        "card_number": "1111111111111113",
                        "pin_code": "1113",
                        "is_superuser": True
                    })
        p1 = Product.objects.create(**{
                        "uuid": '5c90f0f9-1847-498e-9900-144fcc45e714',
                        "name": "Product1",
                        "price": 200,
                        "description": "Product1_description",
                        "amount": 10,
                        "user_owner":  u3,
                    })
        p1.buyers.add(u2, u1)
        p2 = Product.objects.create(**{
                        "uuid": '39bc7af2-3961-4f35-a684-837366c7ea8b',
                        "name": "Product2",
                        "price": 1000,
                        "description": "Product2_description",
                        "amount": 2,
                        "user_owner": u2
                    })
        p2.buyers.add(u1, u3)
        p3 = Product.objects.create(**{
                        "uuid": 'b135fffd-01b2-42dc-9e4e-819f4d059606',
                        "name": "Product3",
                        "price": 10000,
                        "description": "Product3_description",
                        "amount": 2,
                        "user_owner": u2
                    })
        p3.buyers.add(u1)
        p4 = Product.objects.create(**{
                        "uuid": 'e9c5efe3-d9ba-4272-9ec2-d4e456e9947a',
                        "name": "Product4",
                        "price": 20000,
                        "description": "Product4_description",
                        "amount": 22,
                        "user_owner": u2
                    })
        p4.buyers.add(u1)
        p5 = Product.objects.create(**{
                        "uuid": '98243280-f4a5-441a-ad39-9856d9d3fbb6',
                        "name": "Product5",
                        "price": 202000,
                        "description": "Product5_description",
                        "amount": 24,
                        "user_owner": u2
                    })
        p5.buyers.add(u3)
        print("Done!")
