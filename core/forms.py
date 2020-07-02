# forms.py 
from django import forms 
from .models import *
  
class ArticleForm(forms.ModelForm): 
  
    class Meta: 
        model = Article 
        fields = ['image', 'title', 'preview', 'content'] 
