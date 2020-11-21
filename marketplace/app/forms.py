from django import forms
from .models import Produtos

class Product_Form(forms.Form):
    nome_produto = forms.CharField(max_length=100, 
    widget=forms.TextInput(
        attrs={'class':'form-control',
        'placeholder':'Insira um produto'}))

    qtd_estoque = forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control',
        'placeholder':'Quantidade em estoque'}))
    
    preco = forms.FloatField(widget=forms.TextInput(
        attrs={'class':'form-control',
        'placeholder':'Valor do produto'}))

    class Meta:
        Model = Produtos
        fields = ('id_produto','nome_produto','qtd_estoque','preco')