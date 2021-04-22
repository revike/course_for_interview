from django import forms
from test_app.models import GoodItem


class GoodsCreateForm(forms.ModelForm):

    class Meta:
        model = GoodItem
        fields = ('title', 'price', 'vendor', )
