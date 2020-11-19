from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import MarketPlace_List
from .forms import Form_input

def home(request):#Queremos que o vendedor faça login

@require_POST
def add_product(request):
    