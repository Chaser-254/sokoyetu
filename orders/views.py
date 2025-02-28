from django.shortcuts import render, get_object_or_404
from decimal import Decimal

from .models import OrderItem, Order, Product
from .forms import OrderCreateForm
from cart.views import get_cart, cart_clear

def order_create(request):
    cart = get_cart(request)
    cart_qty = sum(item['quantity'] for item in cart.values())

    cart_total = sum(Decimal(item['price']) * Decimal(item['quantity']) for item in cart.values())

    transport_cost = Decimal(round((50 + (cart_qty // 10) * 1.5), 2))

    total_cost = cart_total + transport_cost

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            cf = order_form.cleaned_data
            transport = cf['transport']

            if transport == 'Recipient pickup':
                transport_cost = Decimal(0)

            total_cost = cart_total + transport_cost

            order = order_form.save(commit=False)
            order.transport_cost = transport_cost
            order.total_cost = total_cost
            order.save()

            product_ids = cart.keys()
            products = Product.objects.filter(id__in=product_ids)

            for product in products:
                cart_item = cart[str(product.id)]
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=Decimal(cart_item['price']),
                    quantity=cart_item['quantity']
                )

            cart_clear(request) 
            return render(request, 'orders/order_created.html', {'order': order, 'total_cost': total_cost})

    else:
        order_form = OrderCreateForm()

        if request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile:
                initial_data = {
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'telephone': profile.phone_number,
                    'address': profile.address,
                    'postal_code': profile.postal_code,
                    'city': profile.city,
                    'country': profile.country,
                }
                order_form = OrderCreateForm(initial=initial_data)

    return render(request, 'orders/order_create.html', {
        'cart': cart,
        'order_form': order_form,
        'transport_cost': transport_cost,
        'cart_total': cart_total,
        'total_cost': total_cost,
    })
