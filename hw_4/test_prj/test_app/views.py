from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
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


class GoodsCreateView(CreateView):
    model = GoodItem
    template_name = 'test_app/create_goods.html'
    success_url = reverse_lazy('test_app:goods')
    form_class = GoodsCreateForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
