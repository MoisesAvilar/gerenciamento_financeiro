from django.urls import path
from . import views

app_name = 'cria_lista'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('lista/<int:id_lista>/', views.DetalheListaView.as_view(), name='detalhe_lista'),

    path('lista/nova/', views.ListaCreateView.as_view(), name='nova_lista'),
    path('lista/<int:id_lista>/editar/', views.ListaUpdateView.as_view(), name='editar_lista'),
    path('lista/<int:id_lista>/deletar/', views.ListaDeleteView.as_view(), name='deletar_lista'),

    path('lista/<int:id_lista>/share/', views.share_list_view, name='share_list'),

    path('transacao/<int:id_transacao>/editar/', views.TransacaoUpdateView.as_view(), name='editar_transacao'),
    path('transacao/<int:id_transacao>/deletar/', views.TransacaoDeleteView.as_view(), name='deletar_transacao'),

    path('categorias/', views.CategoriaListView.as_view(), name='categorias'),
    path('categorias/nova/', views.CategoriaCreateView.as_view(), name='nova_categoria'),
    path('categorias/<int:id_categoria>/editar/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/<int:id_categoria>/deletar/', views.CategoriaDeleteView.as_view(), name='deletar_categoria'),
]
