from django.db.models.signals import post_save
from django.db.models import Sum
from products.models.product_models import Product


def send_message(message):
    """
    Note: was not sure how send message to user so for now just print it in console
    """
    print(message)


@post_save(Product)
def send_user_message(sender, instance, created):
    """
    Send user a message after Product save
    """
    user_products = Product.objects.filter(user=instance.user)
    send_message(f"Product_amount: {len(user_products)}, Overall sum: {user_products.annotate(Sum('price'))}")
