from django.db import transaction
from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from cria_lista.forms import AtualizaNomeListaForm, CadastraItensForm, CriaListaForm, EditarItemForm
from cria_lista.models import Item, Lista


class IndexView(generic.TemplateView):
    template_name = 'cria_lista/index.html'


class NovaLista(generic.CreateView):
    model = Lista
    form_class = CriaListaForm
    template_name = 'cria_lista/form_lista.html'
    success_url = reverse_lazy('cria_lista:listas')
    context_object_name = 'lista'


class Listas(generic.ListView):
    model = Lista
    template_name = 'cria_lista/listas.html'
    context_object_name = 'listas'


class VerItens(generic.ListView):
    template_name = 'cria_lista/itens.html'
    context_object_name = 'itens'

    def get_queryset(self):
        id_lista = self.kwargs['id_lista']
        lista = get_object_or_404(Lista, id=id_lista)
        return lista.item_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_lista = self.kwargs['id_lista']
        lista = get_object_or_404(Lista, id=id_lista)
        context['lista'] = lista
        return context


class CadastrarItens(generic.CreateView):
    model = Item
    form_class = CadastraItensForm
    template_name = 'cria_lista/cadastrar_itens.html'

    def form_valid(self, form):
        id_lista = self.kwargs['id_lista']
        lista = Lista.objects.get(id=id_lista)
        item: Item = form.save(commit=False)
        item.lista = lista
        item.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        id_lista = self.kwargs['id_lista']
        lista = Lista.objects.get(id=id_lista)
        itens = Item.objects.filter(lista=lista)
        context['itens'] = itens
        context['lista'] = lista
        return context

    def get_success_url(self):
        id_lista = self.kwargs['id_lista']
        return reverse('cria_lista:cadastrar_itens', kwargs={'id_lista': id_lista})


class EditarLista(generic.UpdateView):
    model = Lista
    form_class = AtualizaNomeListaForm
    template_name = 'cria_lista/form_lista.html'
    context_object_name = 'lista'
    pk_url_kwarg = 'id_lista'

    def get_success_url(self):
        id_lista = self.kwargs['id_lista']
        return reverse('cria_lista:listas')


class EditarItem(generic.UpdateView):
    model = Item
    template_name = 'cria_lista/editar_item.html'

    def get(self, request, id_lista, id_item):
        lista = get_object_or_404(Lista, id=id_lista)
        item = get_object_or_404(Item, id=id_item)
        form = EditarItemForm(instance=item)
        context = {'lista': lista, 'item': item, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, id_lista, id_item):
        lista = get_object_or_404(Lista, id=id_lista)
        item = get_object_or_404(Item, id=id_item)
        form = EditarItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('cria_lista:ver_itens', kwargs={'id_lista': self.kwargs['id_lista']})


class DeletarItem(generic.DeleteView):
    model = Item
    template_name = 'cria_lista/deletar_item.html'
    context_object_name = 'item'

    def get(self, request, id_lista, id_item):
        lista = get_object_or_404(Lista, id=id_lista)
        item = get_object_or_404(Item, id=id_item)
        return render(request, self.template_name, {'lista': lista, 'item': item})

    def post(self, request, id_lista, id_item):
        item = get_object_or_404(Item, id=id_item)
        item.delete()
        return redirect(reverse('cria_lista:ver_itens', kwargs={'id_lista': id_lista}))


class DeletarLista(generic.DeleteView):
    model = Lista
    template_name = 'cria_lista/deletar_lista.html'
    context_object_name = 'lista'
    pk_url_kwarg = 'id_lista'

    def get_success_url(self):
        id_lista = self.kwargs['id_lista']
        return reverse('cria_lista:listas')
