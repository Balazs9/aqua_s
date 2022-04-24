from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        product_types = [(c.id, c.get_product_type()) for c in categories]

        self.fields['category'].choices = product_types
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'