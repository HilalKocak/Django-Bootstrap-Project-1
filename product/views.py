from django.shortcuts import render
from .fakedb.products import FAKE_DB_PRODUCTS
from django.http import Http404
# Create your views here.

def product_list_view(request):
    context = dict(
        products=FAKE_DB_PRODUCTS,
    )
    return render(request, 'product/products.html', context) # we can use html pages in the views

def product_detail_view(request, id):
    result = list(filter(lambda row: (row['id']== id), FAKE_DB_PRODUCTS))

    if result:
        context = dict(
            item =result[0],
            products=FAKE_DB_PRODUCTS,
        )
        return render(request, 'product/product_detail.html', context) # we can use html pages in the views
    raise Http404