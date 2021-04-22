from django.urls import path

from .views import IndexView, GoodsListView, create_form_view

app_name = 'test_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('goods/', GoodsListView.as_view(), name='goods'),
    path('goods/create/', create_form_view, name='good_create'),
]
