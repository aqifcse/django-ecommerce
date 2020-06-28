from django.urls import path
from .views import (
    index,
    blog,
    cart,
    category,
    checkout,
    contact,
    elements,
    singleblog,
    singleproduct,
    tracking
)

app_name= 'core'

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('cart/', cart, name='cart'),
    path('category/', category, name='category'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('single-blog/', singleblog, name='singleblog'),
    path('single-product/', singleproduct, name='singleproduct'),
    path('tracking/', tracking, name='tracking')     
]
