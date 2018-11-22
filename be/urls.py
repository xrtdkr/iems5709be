"""ierg4210Be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from be import views
from be import admin_views

urls = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^getCate/$', views.get_categories),
    url(r'^getProductionIds/$', views.get_commodity_ids),
    url(r'^getProductionById/$', views.get_production_by_id),
    url(r'^getCommodity$', views.get_commodity),

    url(r'^category/get/$', admin_views.category_get),
    url(r'^category/add/$', admin_views.category_add),
    url(r'^category/delete/$', admin_views.category_delete),
    url(r'^category/update/$', admin_views.category_update),

    url(r'^production/get/$', admin_views.production_get),
    url(r'^production/add/$', admin_views.production_add),
    url(r'^production/delete/$', admin_views.production_delete),
    url(r'^production/update/$', admin_views.production_update),
]
