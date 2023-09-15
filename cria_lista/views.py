from django.db import transaction
from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from cria_lista.forms import AtualizaNomeListaForm, CadastraItensForm, CriaListaForm
from cria_lista.models import Item, Lista


class IndexView(generic.TemplateView):
    template_name = 'cria_lista/index.html'


class CriaListaView(generic.CreateView):
    model = Lista
    form_class = CriaListaForm
    template_name = 'cria_lista/criando_lista.html'
    success_url = reverse_lazy('cria_lista:ver_listas')


class VerListasView(generic.ListView):
    model = Lista
    template_name = 'cria_lista/ver_listas.html'
    context_object_name = 'listas'


class CadastrarItensView(generic.CreateView):
    model = Item
    form_class = CadastraItensForm
    template_name = 'cria_lista/cadastrar_itens.html'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        lista = Lista.objects.get(pk=pk)
        item: Item = form.save(commit=False)
        item.lista = lista
        item.save()

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('cria_lista:cadastrar_itens', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        lista = Lista.objects.get(pk=pk)
        itens = Item.objects.filter(lista=lista)
        context['itens'] = itens
        context['lista'] = lista
        return context


class EditarListaView(generic.UpdateView):
    model = Lista
    form_class = AtualizaNomeListaForm
    template_name = 'cria_lista/editar_lista.html'
    context_object_name = 'lista'

    def get_success_url(self):
        return reverse_lazy('cria_lista:ver_listas')


'''def editar_lista_view(request, lista_id):
    listas = get_object_or_404(Lista, id=lista_id)
    if request.method == 'POST':
        novo_nome = request.POST.get('novo_nome')
        listas.nome = novo_nome
        listas.save()
        return redirect('cria_lista:editar_lista', lista_id=listas.id)
    return render(request, 'cria_lista/editar_lista.html',
                  {'listas': listas})'''


class DeletarLista(generic.DeleteView):
    model = Lista
    success_url = reverse_lazy('cria_lista:excluir_lista')
    template_name = 'cria_lista/confirma_excluir_lista.html'
    context_object_name = 'lista'


class DeletarItem(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('cria_lista:excluir_item')
    template_name = 'cria_lista/confirma_excluir_item.html'


def excluir_item_view(request):
    itens = Item.objects.all()
    return render(request, 'cria_lista/excluir_item.html',
                  {'itens': itens})
