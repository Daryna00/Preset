from django import forms
from .models import Merchandise


class MerchanForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = ('name', 'about_preset', 'product', 'before_img','height_field1', 'width_field1',  'after_img', 'height_field2', 'width_field2', 'draft', 'cost')
