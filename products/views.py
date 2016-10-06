from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .models import Product, Category
# Create your views here.


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def productlist_by_category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'products/productlist_by_category.htm',
        {
            'category': category,
            'categories': categories,
            'products': products,
        })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'products/product_detail.html',
        {
            'product': product,
        })
