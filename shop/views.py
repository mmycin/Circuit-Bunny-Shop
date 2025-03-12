from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import json
from .models import Item, CartItem, Announcement, Preorder, Order, OrderUpdate
from .form import formEvent

def home(request):
    items = Item.objects.all()
    sliders = Announcement.objects.all()
    
    form, query, products = formEvent(request)
    category = []
    for item in items:
        category.append(item.Category)

    category = list(set(category))
    print(request.user.is_authenticated)
    context = {
        "items": items,
        "sliders": sliders,
        "form": form,
        "query": query,
        "products": products,
        "categories": category
    }
    return render(request, "home.html", context)

def details(request, id):
    item = get_object_or_404(Item, id=id)
    form, query, products = formEvent(request)
    context = {
        "item": item,
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, "details.html", context)

def search(request):
    form, query, products = formEvent(request)
    context = {
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, 'search.html', context)

def about(request):
    form, query, products = formEvent(request)
    context = {
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, 'about.html', context)

def add_to_cart(request, id):
    product = get_object_or_404(Item, id=id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.Title} is Added to cart")
    return redirect("Cart")

def checkout(request):
    form, query, products = formEvent(request)

    thank = False  # Initialize thank outside of the if block
    if request.method == "POST":
        items = request.POST.get("itemJson", '')
        price = request.POST.get("priceField", '')
        name = request.POST.get("name", '')
        address = request.POST.get("address", '')
        email = request.POST.get("email", '')
        phone = request.POST.get("phone", '') 
        print(items)
        order = Order(Full_name=name, Address=address, Email=email, Phone_number=phone, items=items, TotalPrice=price)
        order.save()
        id = order.id
        price = order.TotalPrice
        print(price)
        print(id)
        update = OrderUpdate(Order_ID=order.id, Description=f"The order has been placed. Price: ৳{order.TotalPrice} ")
        update.save()
        thank = True

    context = {
            "form": form,
            "query": query,
            "products": products,
            "thank": thank,
            "id": id if thank else None  # Only include id if thank is True
        }

    return render(request, 'checkout.html', context)

def preorder(request, queryRes):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone") 
        productname = queryRes

        order = Preorder(Full_name=name, Address=address, Email=email, Phone_number=phone, Name=productname)
        order.save()
        redirect("Home")
    form, query, products = formEvent(request)
    context = {
        "queryRes": queryRes,
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, "preorder.html",context)

def orders(request):
    items = Preorder.objects.all()[::-1]
    orders = Order.objects.all()[::-1]
    if request.user.is_authenticated and request.user.is_staff:
        form, query, products = formEvent(request)
        context = {
            "items":  items,
            "orders": orders,
            "form": form,
            "query": query,
            "products": products
        }
        return render(request, "orders.html", context)
    else:
        return HttpResponse('You don\'t the permission to access this page <a href="/admin" target="_blank">Sign in</a>')
    
def orderdetails(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        order = get_object_or_404(Order, id=id)
        form, query, products = formEvent(request)
        context = {
            "id": id,
            "order": order,
            "form": form,
            "query": query,
            "products": products
        }
        return render(request, "adminorders.html", context)
    else:
        return HttpResponse('You don\'t the permission to access this page <a href="/admin" target="_blank">Sign in</a>')

def preorderdetails(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        item = get_object_or_404(Preorder, id=id)
        form, query, products = formEvent(request)
        context = {
            "id": id,
            "item": item,
            "form": form,
            "query": query,
            "products": products
        }
        return render(request, "adminpreorders.html", context)
    else:
        return HttpResponse('You don\'t the permission to access this page <a href="/admin" target="_blank">Sign in</a>')

def custom_404(request, exception):
    form, query, products = formEvent(request)
    context = {
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, '404.html', context, status=404)

def custom_500(request):
    form, query, products = formEvent(request)
    context = {
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, '500.html', context, status=500)

def tracker(request):
    form, query, products = formEvent(request)

    if request.method == "POST":
        orderID = request.POST.get("orderID", '')
        email = request.POST.get("email", '')

        try:
            order = Order.objects.filter(id=orderID, Email=email)
            print(order)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(Order_ID=orderID)
                updates = []
                for item in update:
                    updates.append({
                        "text": item.Description,
                        "time": item.Timestamp
                    })
                    updatesFinal = list(updates)[::-1]
                    print(updatesFinal)
                    response = json.dumps(updatesFinal, default=str)
                return HttpResponse(response)
            else: 
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")

    context = {
        "form": form,
        "query": query,
        "products": products
    }
    return render(request, 'tracker.html', context)
