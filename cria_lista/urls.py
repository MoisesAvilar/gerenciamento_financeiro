from django.urls import path
from cria_lista import views

app_name = 'cria_lista'
urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('criando-lista/', views.CriaListaView.as_view(), name='criando_lista'),
     path('cadastrar-itens/<int:pk>/', views.CadastrarItensView.as_view(), name='cadastrar_itens'),
     path('ver-listas/', views.VerListasView.as_view(), name='ver_listas'),
     path('editar-lista/<int:pk>/', views.EditarListaView.as_view(),name='editar_lista'),
     path('confirma-excluir-lista/<int:pk>/', views.DeletarLista.as_view(), name='confirma_excluir_lista'),
     path('excluir-item/', views.excluir_item_view, name='excluir_item'),
     path('confirma-excluir-item/<pk>/', views.DeletarItem.as_view(), name='confirma_excluir_item'),
]
