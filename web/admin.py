from django.contrib import admin
from . models import Tb_estoque, Tb_cliente, Tb_usuario, Tb_fornecedor, Tb_vendas
# Register your models here.

admin.site.register(Tb_estoque)
admin.site.register(Tb_cliente)
admin.site.register(Tb_usuario)
admin.site.register(Tb_fornecedor)
admin.site.register(Tb_vendas)