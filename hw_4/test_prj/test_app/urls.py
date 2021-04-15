from django.urls import path

from .views import IndexView, GoodsListView, GoodsCreateView

app_name = 'test_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('goods/', GoodsListView.as_view(), name='goods'),
    path('goods/create', GoodsCreateView.as_view(), name='create_goods'),
]
