from django import template
from portfolio.models import Page, Slider
register = template.Library()

@register.inclusion_tag('page/pages_menu.html')
def show_pages_menu(pages_menu):
    pages_menu = Page.objects.all()
    return { 'pages_menu' : pages_menu }

#add tag for home slider
@register.inclusion_tag('slider.html')
def show_slides(slides):
    slides = Slider.objects.all()
    return { 'slides' : slides }
