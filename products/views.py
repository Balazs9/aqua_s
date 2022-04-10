from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def mineral_water(request):
    """ A view to show only the mineral waters """

    products = Product.objects.filter(category__name=mineral_water)

    return render(request, 'products/products.html', {
        'products': products,
    })


def sport_drink(request):
    """ A view to show only the sport drinks """

    products = Product.objects.filter(category__name=sport_drink)

    return render(request, 'products/products.html', {
        'products': products,
    })


def water_dispenser(request):
    """ A view to show only the water dispenser machines """

    products = Product.objects.filter(category__name=water_dispenser)

    return render(request, 'products/products.html', {
        'products': products,
    })


def product_detail(request, product_id):
    """ A view to show informations about the product """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)
