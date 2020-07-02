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
    path('singleblog/<int:id>/', singleblog, name='singleblog'),
    path('single-product/', singleproduct, name='singleproduct'),
    path('tracking/', tracking, name='tracking'),

    path('archive/', ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name="article_archive")    
]
