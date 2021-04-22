from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from .forms import GoodsCreateForm
from .models import GoodItem


class IndexView(TemplateView):
    template_name = 'test_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'главная'
        return context


class GoodsListView(ListView):
    model = GoodItem
    template_name = 'test_app/goods_list.html'
    context_object_name = 'goods'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товары'
        return context


# Переделал на функцию, для бОльшей простоты и наглядности
# формсет тоже убрал, оставил использование простой формы.
# с формсетами на порядок сложнее работать и надо сначала понять как
# простые формы работают
def create_form_view(request):
    if request.method == 'POST':
        form = GoodsCreateForm(request.POST)
        if form.is_valid():
            form.save()
        # если это был POST запрос, то мы возвращаем в ответе HTML таблицы товаров
        # если новый товар был успешно создан, то он уже попадет в GoodItem.objects.all()
        # и отобразится в таблице товаров
        return render(request, template_name='test_app/goods_table.html', context={'goods': GoodItem.objects.all()})
    # Если это был GET запрос, то возвращаем HTML формы добавления нового товара
    return render(request, template_name='test_app/gooditem_form.html', context={'form': GoodsCreateForm()})
