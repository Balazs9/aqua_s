from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    """ A view to show all products """

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show informations about the product """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)
