from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.staticfiles.urls import *
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from solid_i18n.urls import solid_i18n_patterns
from django.utils.translation import ugettext_lazy as _

from products import views

urlpatterns = patterns (
        '',
        url(r'^categories/$', views.category_list, name='category_list'),
        url(r'^categories/(?P<category_slug>[-\w]+)/$', views.productlist_by_category, name='productlist_by_category'),
        url(r'^product/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
)
