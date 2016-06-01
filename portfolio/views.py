from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .models import Project, Product, Faq, Page, Category


def home(request):
    output = _("Welcome to my site.")
    return render(request, 'home.html', {'output': output})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def faq(request):
    faqs = Faq.objects.all()
    categories = Category.objects.all()
    return render(request, 'faq.html', {
        'faqs': faqs,
        'categories': categories,
        })


def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})


def portfolio_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'project': project})


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

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page/page_detail.html', {'page': page })
