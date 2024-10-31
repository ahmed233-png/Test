from django import forms
from . models import MyProduct
class CreateNewProduct(forms.ModelForm):
    class Meta:
        model=MyProduct
        fields=['name','description','price','quantity','photo','create_by']

    def __init__(self, *args, **kwargs):
        super(CreateNewProduct,self).__init__(*args, **kwargs)
        self.fields['create_by'].empty_label = "Select"
      
