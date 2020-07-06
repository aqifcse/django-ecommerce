from django.conf import settings
from django.db import models
from django.urls import reverse

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



