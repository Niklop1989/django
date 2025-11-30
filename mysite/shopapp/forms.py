from django import forms

from shopapp.models import Product

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('widget',MultipleFileInput())
        super().__init__(*args,**kwargs)

    def clean(self, data, initial = None):
        single_file_clean = super().clean
        if isinstance(data,(list,tuple)):
            result = [single_file_clean(d, initial)for d in data]
        else:
            result = [single_file_clean(data,initial)]
        return result

class FileFieldForm(forms.Form):
    file_field = MultipleFileField()

class ProductForm(forms.ModelForm):

    class Meta:
        from shopapp.models import Product
        model =Product
        fields = 'name','price','description','discount','preview','images'

    images = MultipleFileField(required=False,
                                 label='images')

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
