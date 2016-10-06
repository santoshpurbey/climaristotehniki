
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

from pages import views

urlpatterns = patterns (
        '',
        # url(r'^contact/$', views.contact, name='contact'),
        url(r'^page/(?P<pk>[0-9]+)/$', views.page_detail, name='page_detail'),
        url(r'^faq/$', views.faq, name='faq'),

)
