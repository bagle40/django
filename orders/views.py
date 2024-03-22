import uuid
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from yookassa import Payment,Configuration
from django.conf import settings

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                            coment_order=form.cleaned_data['coment_order'],
                        )

                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.products_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе. В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()




                        # Оплата через YooKassa
                        idempotence_key = uuid.uuid4()
                        total_price = cart_item.products_price()
                        currency = 'RUB'
                        description = 'Оплата товаров из корзины'

                        payment = Payment.create({
                            'amount': {
                                'value': str(total_price),
                                'currency': currency
                            },
                            'confirmation': {
                                'type': 'redirect',
                                'return_url': request.build_absolute_uri(reverse('user:profile'))
                            },
                            'capture': True,
                            'test': True,
                            'description': description
                        }, idempotence_key)

                        confirmation_url = payment.confirmation.confirmation_url
                        cart_items.delete()
                        return redirect(confirmation_url)

            except ValidationError as e:
                return redirect('cart:order')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)