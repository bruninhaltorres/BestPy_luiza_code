from django import forms

class Form_input(forms.Form):
    nome_produto = forms.CharField(max_length=100,
    widget=forms.Input( # TextInput() ?
        attrs={
            'class': 'form-control',
            'placeholder': 'Nome produto'
        }
    ))
    qtd_estoque = forms.IntegerField( ,
    widget=forms.Input(
        attrs={
            'class': 'form-control',
            'placeholder': 'Quantidade em estoque'
        }
    ))
    preco = forms.IntegerField( ,
    widget=forms.Input(
        attrs={
            'class': 'form-control',
            'placeholder': 'Valor do produto'
        }
    ))
    foto_produto = forms.ImageField()
 

