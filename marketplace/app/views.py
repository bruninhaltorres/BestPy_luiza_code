from django.shortcuts import render, redirect
from .forms import Product_Form, Produto_Form, Vendedor_Form
from .models import Produtos
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    Produto = Produtos.objects.order_by('id_produto')
    context = {
        'Produtos':Produto,
    }
    return render(request,'app/index.html',context)

def login_user(request):
    return render(request, 'login.html')

def add_product(request):
    if request.method == 'POST':
        form = Produto_Form()
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('/')
    else: 
        form = Produto_Form()
        return render(request,'app/add_product.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = Vendedor_Form()
        if form.is_valid():
            vendedor = form.save(commit=False)
            vendedor.save()
            return redirect('/')
    else: 
        form = Vendedor_Form()
        return render(request,'app/add_user.html', {'form': form})

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