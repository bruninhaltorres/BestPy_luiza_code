from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import Product_Form
from .models import Produtos
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    my_item = Produtos.objects.order_by('id_produto')
    form = Product_Form()
    context = {
        'my_item':my_item,
        'form': form
    }
    return render(request,'app/index.html',context)