from cpf_field.models import CPFField
from django.db import models

# Create your models here.
from phone_field import PhoneField


class Tb_estoque(models.Model):
    id_estoque = models.IntegerField(primary_key=True, verbose_name='Id estoque')
    id_produto = models.IntegerField(verbose_name='Id produto', null=True)
    ds_n = models.CharField(max_length=45, verbose_name='Nome')
    ds_tamanho = models.CharField(max_length=2, verbose_name='Tamanho', null=True)
    ds_cor = models.CharField(max_length=10, verbose_name='Cor', null=True)
    vl_preco_custo = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Custo',null=True)
    vl_preco_venda = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Preco de venda', null=True)
    dt_entrada = models.DateField(verbose_name='Data de entrada', null=True)

class Tb_cor(models.Model):
    cor = models.CharField(max_length=45)

class Tb_cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = CPFField('cpf')
    cep = models.IntegerField(verbose_name='CEP')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    uf = models.CharField(max_length=2, verbose_name='Uf')
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')

class Tb_usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = CPFField('cpf')
    cep = models.IntegerField(verbose_name='CEP')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    email = models.EmailField()
    telefone = PhoneField(blank=True, help_text='Contact phone number')
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')

class Tb_fornecedor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cnpj = models.IntegerField(verbose_name='CNPJ')
    cep = models.IntegerField(verbose_name='CEP')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    email = models.EmailField()
    telefone = PhoneField(blank=True, help_text='Contact phone number')
    codigo = models.IntegerField(verbose_name='Codigo do produto')
    tipo = models.CharField(max_length=45, verbose_name='Tipo: Blusa / Saia / Calça')

class Tb_vendas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do cliente')
    cpf = CPFField('cpf do cliente')
    valor = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do pedido', null=True)
    cep = models.IntegerField(verbose_name='CEP do cliente')
    endereco = models.CharField(max_length=200, verbose_name='Endereço do cliente')
    dt = models.DateField(verbose_name='Data do pedido')
    codigo = models.IntegerField(verbose_name='Codigo do produto')
    status = models.CharField(max_length=45, verbose_name='Status: Separando / Processando / Entregue / Cancelado')

