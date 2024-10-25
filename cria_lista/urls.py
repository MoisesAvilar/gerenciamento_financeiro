from django.urls import path
from cria_lista import views


app_name = 'cria_lista'
urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('nova-lista/', views.NovaLista.as_view(), name='nova_lista'),
     path('listas/', views.Listas.as_view(), name='listas'),
     path('listas/<int:id_lista>/cadastrar/', views.CadastrarItens.as_view(), name='cadastrar_itens'),
     path('listas/<int:id_lista>/editar/', views.EditarLista.as_view(), name='editar_lista'),
     path('listas/<int:id_lista>/deletar/', views.DeletarLista.as_view(), name='deletar_lista'),
     path('listas/<int:id_lista>/item/', views.VerItens.as_view(), name='ver_itens'),
     path('listas/<int:id_lista>/item/editar/<int:id_item>/', views.EditarItem.as_view(), name='editar_item'),
     path('listas/<int:id_lista>/item/deletar/<int:id_item>/', views.DeletarItem.as_view(), name='deletar_item'),
     path('listas/<int:id_lista>/export-to-excel/', views.export_to_excel, name='export_to_excel'),

]
