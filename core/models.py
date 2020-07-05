from django.conf import settings
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ('TS', 'Tshirt'),
    ('SK', 'Sneaker'),
    ('WH', 'Watch'),
    ('HB', 'Handbag'),
    ('JS', 'Jeans')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    category = models.CharField(choices=LABEL_CHOICES, max_length=2)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Article Model
class Article(models.Model):
  
    title = models.CharField(max_length=200)
    preview = models.TextField(max_length=500)
    content = models.TextField(max_length=1000)
    pub_date = models.DateField()
    image = models.FileField(blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    
    previous_article = models.OneToOneField('self',
                                 related_name='previous_post',
                                 blank=True,
                                 null=True,
                                 on_delete=None)

    next_article = models.OneToOneField('self',
                                 related_name='next_post',
                                 blank=True,
                                 null=True,
                                 on_delete=None)

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title



