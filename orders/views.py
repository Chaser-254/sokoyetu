from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order, Product
from .forms import OrderCreateForm
from cart.views import get_cart, cart_clear
from decimal import Decimal

def order_create(request):
    cart = get_cart(request)
    cart_qty = sum(item['quantity'] for item in cart.values())

    # Calculate the total price of items in the cart
    cart_total = sum(Decimal(item['price']) * Decimal(item['quantity']) for item in cart.values())

    # Default transport cost calculation
    transport_cost = Decimal(round((50 + (cart_qty // 10) * 1.5), 2))

    # Default total cost (cart total + transport cost)
    total_cost = cart_total + transport_cost

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            cf = order_form.cleaned_data
            transport = cf['transport']

            if transport == 'Recipient pickup':
                transport_cost = Decimal(0)  # Free transport

            total_cost = cart_total + transport_cost  # Ensure total is updated

            order = order_form.save(commit=False)
            order.transport_cost = transport_cost
            order.total_cost = total_cost
            order.save()

            # Create order items
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

            cart_clear(request)  # Clear cart after order creation
            return render(request, 'orders/order_created.html', {'order': order, 'total_cost': total_cost})

    else:
        order_form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {
        'cart': cart,
        'order_form': order_form,
        'transport_cost': transport_cost,
        'cart_total': cart_total,
        'total_cost': total_cost,  # Pass total cost to template
    })
