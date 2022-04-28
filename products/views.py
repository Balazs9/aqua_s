from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .forms import ProductForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def mineral_water(request):
    """ A view to show only the mineral waters """

    product = Product.objects.filter(category__name='mineral_water')

    return render(request, 'products/products.html', {
        'products': product,
    })


def sport_drink(request):
    """ A view to show only the sport drinks """

    product = Product.objects.filter(category__name='sport_drink')
    return render(request, 'products/products.html', {
        'products': product,
    })


def water_dispenser(request):
    """ A view to show only the water dispenser machines """

    product = Product.objects.filter(category__name='water_dispenser')

    return render(request, 'products/products.html', {
        'products': product,
    })


def product_detail(request, product_id):
    """ A view to show informations about the product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add product.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add product.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'editing {product.name}')
        
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete product from shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add product.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect('products')
