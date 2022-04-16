"""shopback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import product_list,product_detail, category_show, category_detail, categ_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', product_list),
    path('api/products/<int:product_id>/', product_detail),
    path('api/categories/', category_show),
    path('api/categories/<int:categ_id>', category_detail),
    path('api/categories/<cat_id>/products/', categ_id)
]
