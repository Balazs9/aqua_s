from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that show the bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the chosen product to the bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    return redirect(redirect_url)
