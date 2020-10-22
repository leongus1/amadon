from django.shortcuts import render, redirect
from .models import Order, Product


#RENDER
def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    this_order_total = Order.objects.last().total_price
    all_items_from_all_orders = 0
    grand_total = 0
    
    for order in Order.objects.all():
        grand_total+=order.total_price
        all_items_from_all_orders+=order.quantity_ordered
    
    context = {
        'total': this_order_total,
        'items': all_items_from_all_orders,
        'grand_total': grand_total,
    }
    return render(request, "store/checkout.html", context)


#PROCESS DATA
def process_data(request):
    quantity_from_form = int(request.POST["quantity"])
    price = Product.objects.get(id=request.POST['id']).price
    price_from_form = float(float)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
   
    return redirect('/checkout')