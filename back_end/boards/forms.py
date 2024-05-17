from django import forms
from .models import Article, Comment


class PostForm(forms.ModelForm):
    TEAM_CHOICES = [
        ('롯데', '롯데'),
        ('기아', '기아'),
        ('한화', '한화'),
        ('삼성', '삼성'),
        ('키움', '키움'),
        ('KT', 'KT'),
        ('NC', 'NC'),
        ('SSG', 'SSG'),
        ('두산', '두산'),
        ('LG', 'LG')
    ]

    team = forms.ChoiceField(choices=TEAM_CHOICES)

    class Meta:
        model = Article
        fields = ['title', 'team', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
