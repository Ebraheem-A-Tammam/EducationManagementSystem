from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
    #No TITLE DUPLICATE

    
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={"size": "70"}))

    class Meta:
        model = Comment
        fields = ["content"]
