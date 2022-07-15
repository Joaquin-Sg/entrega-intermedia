from django import forms

class ProductoFormulario(forms.Form):

    name_of_product = forms.CharField(required=False)
    price = forms.DecimalField()


class ProductoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()