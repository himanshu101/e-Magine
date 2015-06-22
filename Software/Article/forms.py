from django import forms
from models import *

class ArticleForm(forms.ModelForm):
	class Meta : 
		model = Article
		fields = ['title', 'body', 'tag', 'doc']

class CommentsForm(forms.ModelForm):
	class Meta : 
		model = Comments
		fields =['comment']
