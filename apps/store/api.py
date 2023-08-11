import json

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string


from apps.cart.cart import Cart
from apps.order.views import render_to_pdf

from apps.order.utils import checkout

from .models import Product
from apps.order.models import Order
from apps.coupon.models import Coupon

from .utilities import decrement_product_quantity, send_order_confirmation


def create_checkout_session(request):
    data = json.loads(request.body)

    # Coupon 

    coupon_code = data['coupon_code']
    coupon_value = 0

    if coupon_code != '':
        coupon = Coupon.objects.get(code=coupon_code)

        coupon_value = coupon.value

    cart = Cart(request)
    items = []
    
    for item in cart:
        product = item['product']

        price = int(product.price ) * int(item['quantity'])


        item['price'] = price


    gateway = data['gateway']
    session = ''
    order_id = ''
   
    
    

    # Create order

    orderid = checkout(request, data['first_name'], data['last_name'], data['email'], data['address'], data['zipcode'], data['City'], data['phone'])

    total_price = 0.00
    
    for item in cart:
        product = item['product']
        total_price = total_price + (float(product.price) * int(item['quantity']))
       
   
    if coupon_value > 0:
        total_price = round(total_price * (1-(coupon_value / 100)), 2)
    

   
    order = Order.objects.get(pk=orderid)
    
    order.paid_amount = total_price
    order.used_coupon = coupon_code
    order.save()


    return JsonResponse({'session': session, 'order': ' '})

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    
    return JsonResponse(jsonresponse)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)