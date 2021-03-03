from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'})
    )
    image = forms.ImageField(
        label='Main post image', 
        widget=forms.FileInput(attrs={'class': 'custom-file-input', 'onchange':'imageFileHandler(this.files)'})
    )

    class Meta:
        model = Post
        fields = ['title', 'image', 'content']