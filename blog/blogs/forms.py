from django import forms
from django.urls import reverse
from django.contrib.flatpages.models import FlatPage

from tinymce.widgets import TinyMCE

from .models import Blog


# class FlatPageForm(forms.ModelForm):
#     content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

#     class Meta:
#         model = FlatPage

class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False


class BlogForm(forms.ModelForm):
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/')
    content = HTMLField()
    """
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    content = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 80, 'rows': 30}))

    class Meta:
        model = Blog
        fields = '__all__'