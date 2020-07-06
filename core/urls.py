from django.urls import path
from django.views.generic.dates import ArchiveIndexView

from core.models import Article

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
    tracking,

    OrderSummaryView,
    ItemDetailView,
    add_to_cart,
    AddCouponView,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    RequestRefundView

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
    path('singleblog/<int:id>/', singleblog, name='singleblog'),
    path('single-product/', singleproduct, name='singleproduct'),
    path('tracking/', tracking, name='tracking'),

    path('archive/', ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name="article_archive"),

    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')   
]
