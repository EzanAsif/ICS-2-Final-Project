from django import forms
from . import models

class Createreview(forms.ModelForm):
    class Meta:
        model = models.review
        fields = ['title', 'body', 'slug', 'thumb', 'bookAuth']