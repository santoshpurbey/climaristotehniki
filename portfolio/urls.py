
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

from portfolio import views

urlpatterns = patterns ('',
        url(r'^$', views.home, name='home'),
        url(r'^about/$', views.about, name='about'),
        url(r'^work/$', views.portfolio_list, name='portfolio_list'),
        url(r'^faq/$', views.faq, name='faq'),
        url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
        # url(r'^categories/$', views.category_list, name='category_list'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^page/(?P<pk>[0-9]+)/$', views.page_detail, name='page_detail'),
)
