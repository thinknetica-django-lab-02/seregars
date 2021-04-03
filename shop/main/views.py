from django.shortcuts import render
from django.views import generic

from main.models import *


def index(request):
    turn_on_block = True
    user = request.user
    return render(request, 'main/index.html', {'turn_on': turn_on_block, 'user': user})

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'goods'
    template_name = 'main/goods.html'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/detail_goods.html'