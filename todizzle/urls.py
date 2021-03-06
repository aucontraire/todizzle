"""todizzle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todos import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    
    url(r'^item/(\d+)$', views.item_page, name="item"),
    url(r'^item/(\d+)/complete', views.item_complete, name='item_complete'),
    url(r'^item/(\d+)/archive', views.item_archive, name='item_archive'),
    url(r'^item/(\d+)/delete', views.item_delete, name='item_delete'),
    
    url(r'^tags$', views.TagsView.as_view(), name='tags_view'),
    url(r'^tag/(\d+)$', views.tag_view, name='tag_view'),
    
    url(r'^admin/', admin.site.urls),
]
