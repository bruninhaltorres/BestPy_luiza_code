from django.contrib import admin
from .models import Vendedor, Produtos

# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Produtos)