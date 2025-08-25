from django.shortcuts import render

def shopping(request):
    return render(request, "store/shopping.html")

def cart(request):
    return render(request, "store/cart.html")

def payment(request):
    return render(request, "store/payment.html")
