from django.shortcuts import render, redirect
from .forms import Product_Form
from .models import Produtos
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def list_all(request):
    produtos = Produtos.objects.filter(ativo=True)
    return render(request, 'list.html', {'Produtos': produtos})

def app_detail(request, id_produto):
    produtos = Produtos.objects.get(ativo=True, id_produto = id_produto)
    print(produtos.id_produto)
    return render(request, 'detail.html', {'Produtos': produtos})

def cadastro(request):
    return render(request, 'cadastro.html')

@login_required(login_url='/login/')
def set_produto(request):
    nome = request.POST.get('name')
    print(nome)
    estoque = request.POST.get('estoque')
    preco = request.POST.get('preco')
    produto = Produtos.objects.create(nome_produto=nome, qtd_estoque=estoque, preco=preco)
    return render(request, 'index.html')

@login_required(login_url='/login/')
def index(request):
    my_item = Produtos.objects.order_by('id_produto')
    form = Product_Form()
    context = {
        'my_item':my_item,
        'form': form
    }
    return render(request,'app/index.html',context)

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
@require_POST
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')