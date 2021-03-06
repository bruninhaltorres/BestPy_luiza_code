from django.shortcuts import render, redirect
from .forms import Product_Form
from .models import Produtos, Vendedor
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def list_all(request):
    produtos = Produtos.objects.filter(ativo = True)
    return render(request, 'list.html', {'Produtos': produtos})

def app_detail(request, id_produto):
    produtos = Produtos.objects.get(ativo=True, id_produto = id_produto)
    return render(request, 'detail.html', {'Produtos': produtos})

def inativar(request, id_produto):
    produtos = Produtos.objects.get(id_produto = id_produto)
    produtos.ativo = False
    produtos.save()
    return render(request, 'index.html', {'Produtos': produtos})

def register(request):
    return render(request, 'register.html')

def set_vendedor(request):
    nome = request.POST.get('name')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    vendedor = Vendedor.objects.create(nome_vendedor=nome, login_vendedor=usuario, email_vendedor=email, senha_vendedor=senha)
    return render(request, 'sucess.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def alterar(request,id_produto):
    produto = Produtos.objects.get(id_produto=id_produto)
    product_form = Product_Form(request.POST or None)
    if product_form.is_valid():
        product_form.save()
    return render(request, 'alterar.html', {'produto': produto})

def update_produto(request, id_produto):
    nome = request.POST.get('nome_produto')
    estoque = request.POST.get('qtd_estoque')
    preco = request.POST.get('preco')
    produtos = Produtos.objects.get(id_produto = id_produto)
    produtos.ativo = False
    produtos.save()
    produto = Produtos.objects.create(nome_produto=nome, qtd_estoque=estoque, preco=preco)
    return render(request, 'index.html')


def consulta_produto(request):
    try:
        nome_produto = request.POST.get('nome_produto')    
        produtos = Produtos.objects.get(nome_produto = nome_produto)
        return render(request, 'consulta.html', {'Produtos': produtos})
    except:
        return render(request, 'consulta_erro.html')


@login_required(login_url='/login/')
def set_produto(request):
    nome = request.POST.get('name')
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