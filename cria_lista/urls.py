from django.urls import path
from cria_lista import views

app_name = 'cria_lista'
urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('editar', views.EditarView.as_view(), name='editar'),
     path('criando-lista/',
          views.CriaListaView.as_view(), name='criando_lista'),
     path(
          'cadastrar-itens/<int:pk>', views.CadastrarItensView.as_view(),
          name='cadastrar_itens'
          ),
     path('ver-listas/',
          views.VerListasView.as_view(), name='ver_listas'),
     path('lista/<int:pk>/', views.ListaView.as_view(), name='lista'),
     path('atualizar-lista/',
          views.atualizar_lista_view, name='atualizar_lista'),
     path('editar-lista/<int:lista_id>/',
          views.editar_lista_view, name='editar_lista'),
     path('excluir/', views.excluir_view, name='excluir'),
     path('excluir-lista/', views.excluir_lista_view,
          name='excluir_lista'),
     path('confirma-excluir-lista/<pk>/', views.DeletarLista.as_view(),
          name='confirma_excluir_lista'),
     path('excluir-item/', views.excluir_item_view, name='excluir_item'),
     path('confirma-excluir-item/<pk>/', views.DeletarItem.as_view(),
          name='confirma_excluir_item'),
     path('escolher-lista', views.EscolherListaView.as_view(),
          name='escolher_lista'),
]
