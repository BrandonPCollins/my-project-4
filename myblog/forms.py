from django import forms 
from .models import Post  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your Title Here!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give your post a tag!'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your Title Here!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give your post a tag!'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }