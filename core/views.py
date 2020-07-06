from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleImage

def index(request):
    blogs = Article.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def blog(request):
    blogs = Article.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def cart(request):
    blogs = Article.objects.all()
    return render(request, 'cart.html')


def category(request):
    blogs = Article.objects.all()
    return render(request, 'category.html')


def checkout(request):
    blogs = Article.objects.all()
    return render(request, 'checkout.html')


def contact(request):
    blogs = Article.objects.all()
    return render(request, 'contact.html')


def elements(request):
    blogs = Article.objects.all()
    return render(request, 'elements.html')


def singleblog(request, id):
    blog = get_object_or_404(Article, id=id)
    photos = ArticleImage.objects.filter(id=id)
    return render(request, 'single-blog.html', {'blog': blog, 'photos':photos})


def singleproduct(request):
    blogs = Article.objects.all()
    return render(request, 'single-product.html')


def tracking(request):
    blogs = Article.objects.all()
    return render(request, 'tracking.html')

