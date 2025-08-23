from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Order, Product, User

# Show all orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


# Show single order details
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})


# Create new order
def order_create(request, user_id, product_id):
    user = get_object_or_404(User, id=user_id)
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        order = Order.objects.create(user=user, product=product, quantity=quantity)
        return redirect('order_detail', order_id=order.id)

    return render(request, 'order_form.html', {'user': user, 'product': product})


# Delete an order
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_list')
