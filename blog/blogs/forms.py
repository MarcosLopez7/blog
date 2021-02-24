from django import forms
from django.urls import reverse

from tinymce.widgets import TinyMCE


class BlogForm(forms.Form):
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/')
    content = HTMLField()
    """
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    content = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': ''}))