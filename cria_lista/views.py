from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404

from .models import Categoria, Lista, Transacao
from .forms import CategoriaForm, ListaForm, TransacaoForm, ShareListForm, TransacaoFilterForm
from django.utils import timezone
from datetime import timedelta


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class IndexView(generic.CreateView):
    model = Transacao
    form_class = TransacaoForm
    template_name = 'cria_lista/index.html'
    success_url = reverse_lazy('cria_lista:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['lista'] = None
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listas'] = Lista.objects.filter(
            Q(user=self.request.user) | Q(shared_with=self.request.user)
        ).distinct().order_by('-data')
        
        context['transacoes_pessoais'] = Transacao.objects.filter(
            user=self.request.user,
            lista=None
        ).order_by('-data')[:10]
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.lista = None
        form.save()
        messages.success(self.request, "Transação pessoal registrada!")
        return super().form_valid(form)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListaCreateView(generic.CreateView):
    """
    Substitui a antiga 'NovaLista'.
    Usa o novo 'ListaForm' para criar um "Envelope".
    """

    model = Lista
    form_class = ListaForm
    template_name = "cria_lista/form_lista.html"
    success_url = reverse_lazy("cria_lista:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request, f"Envelope '{form.instance.nome}' criado com sucesso!"
        )
        return super().form_valid(form)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListaUpdateView(generic.UpdateView):
    """
    Substitui a antiga 'EditarLista'.
    Usa o novo 'ListaForm' para editar um "Envelope".
    """

    model = Lista
    form_class = ListaForm
    template_name = "cria_lista/form_lista.html"
    pk_url_kwarg = "id_lista"
    success_url = reverse_lazy("cria_lista:index")

    def get_queryset(self):
        return Lista.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListaDeleteView(generic.DeleteView):
    """
    Substitui a antiga 'DeletarLista'.
    """

    model = Lista
    pk_url_kwarg = "id_lista"
    template_name = "cria_lista/lista_confirm_delete.html"
    success_url = reverse_lazy("cria_lista:index")

    def get_queryset(self):
        return Lista.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DetalheListaView(generic.CreateView):
    """
    Esta é a view MAIS IMPORTANTE.
    Substitui a antiga 'VerItens' e 'CadastrarItens'.
    - É uma 'CreateView' para o 'TransacaoForm' (Registro Rápido).
    - Também lista todas as transações existentes para esta lista.
    """

    model = Transacao
    form_class = TransacaoForm
    template_name = "cria_lista/detalhe_lista.html"

    def get_lista_object(self):
        """Helper para buscar a lista com permissão e evitar duplicatas"""
        if not hasattr(self, "_lista_object"):
            lista_id = self.kwargs["id_lista"]
            lista = (
                Lista.objects.filter(
                    Q(user=self.request.user) | Q(shared_with=self.request.user),
                    id=lista_id,
                )
                .distinct()
                .first()
            )

            if not lista:
                raise Http404("Lista não encontrada ou você não tem permissão.")
            self._lista_object = lista
        return self._lista_object

    def get_transacoes_queryset(self):
        """Aplica os filtros de tempo, categoria e ordenação à lista de transações."""
        lista = self.get_lista_object()
        queryset = Transacao.objects.filter(lista=lista)
        get_params = self.request.GET

        categoria_id = get_params.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria__id=categoria_id)

        periodo = get_params.get('periodo')
        data_inicio = get_params.get('data_inicio')
        data_fim = get_params.get('data_fim')

        filtro_data = {}
        hoje = timezone.localdate()

        if periodo == 'today':
            filtro_data['data'] = hoje
        elif periodo == 'week':
            filtro_data['data__gte'] = hoje - timedelta(days=7)
        elif periodo == 'month':
            filtro_data['data__year'] = hoje.year
            filtro_data['data__month'] = hoje.month
        elif periodo == 'custom' and data_inicio and data_fim:
            filtro_data['data__range'] = [data_inicio, data_fim]

        queryset = queryset.filter(**filtro_data)

        ordem = get_params.get('ordem')
        if ordem == 'highest':
            queryset = queryset.order_by('-valor', '-data')
        elif ordem == 'lowest':
            queryset = queryset.order_by('valor', '-data')
        elif ordem == 'oldest':
            queryset = queryset.order_by('data')
        else:
            queryset = queryset.order_by('-data')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lista = self.get_lista_object()

        context['filter_form'] = TransacaoFilterForm(self.request.GET, lista=lista)

        context['transacoes'] = self.get_transacoes_queryset()
        context['lista'] = lista
        return context

    def get_form_kwargs(self):
        """
        Passa argumentos extras para o __init__ do TransacaoForm.
        """
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        kwargs["lista"] = self.get_lista_object()
        return kwargs

    def form_valid(self, form):
        lista = self.get_lista_object()

        form.instance.user = self.request.user
        form.instance.lista = lista

        form.save()

        messages.success(self.request, "Transação registrada!")
        return redirect("cria_lista:detalhe_lista", id_lista=lista.id)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class TransacaoUpdateView(generic.UpdateView):
    """
    Nova view para permitir a EDIÇÃO de uma transação.
    """

    model = Transacao
    form_class = TransacaoForm
    template_name = "cria_lista/form_transacao.html"
    pk_url_kwarg = "id_transacao"

    def get_queryset(self):
        return Transacao.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        transacao = self.get_object()
        if transacao.lista:
            return reverse(
                "cria_lista:detalhe_lista", kwargs={"id_lista": transacao.lista.id}
            )
        return reverse("cria_lista:index")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class TransacaoDeleteView(generic.DeleteView):
    """
    Nova view para permitir a EXCLUSÃO de uma transação.
    """

    model = Transacao
    pk_url_kwarg = "id_transacao"
    template_name = "cria_lista/transacao_confirm_delete.html"

    def get_queryset(self):
        return Transacao.objects.filter(user=self.request.user)

    def get_success_url(self):
        transacao = self.get_object()
        if transacao.lista:
            return reverse(
                "cria_lista:detalhe_lista", kwargs={"id_lista": transacao.lista.id}
            )
        return reverse("cria_lista:index")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CategoriaListView(generic.ListView):
    """
    Mostra ao usuário todas as suas categorias pessoais.
    """

    model = Categoria
    template_name = "cria_lista/categoria_list.html"
    context_object_name = "categorias"

    def get_queryset(self):
        return Categoria.objects.filter(user=self.request.user).order_by("nome")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CategoriaCreateView(generic.CreateView):
    """
    Permite ao usuário criar uma nova categoria pessoal.
    """

    model = Categoria
    form_class = CategoriaForm
    template_name = "cria_lista/form_categoria.html"
    success_url = reverse_lazy("cria_lista:categorias")

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except Exception:
            messages.error(self.request, "Você já possui uma categoria com esse nome.")
            return self.form_invalid(form)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "cria_lista/form_categoria.html"
    pk_url_kwarg = "id_categoria"
    success_url = reverse_lazy("cria_lista:categorias")

    def get_queryset(self):
        return Categoria.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    pk_url_kwarg = "id_categoria"
    template_name = "cria_lista/categoria_confirm_delete.html"
    success_url = reverse_lazy("cria_lista:categorias")

    def get_queryset(self):
        return Categoria.objects.filter(user=self.request.user)


@login_required(login_url='accounts:login')
def share_list_view(request, id_lista):
    lista = get_object_or_404(Lista, id=id_lista, user=request.user) 

    if request.method == 'POST':
        form = ShareListForm(request.POST)
        if form.is_valid():
            identificador = form.cleaned_data['identificador']
            try:
                user_to_share = User.objects.filter(
                    Q(email=identificador) | Q(username=identificador)
                ).first()

                if user_to_share:
                    lista.shared_with.add(user_to_share)
                    lista.save()
                    messages.success(request, f'Envelope compartilhado com {identificador}!')
                else:
                    messages.error(request, f'Usuário "{identificador}" não foi encontrado.')

            except Exception as e:
                messages.error(request, f'Ocorreu um erro: {e}')
            
            return redirect('cria_lista:detalhe_lista', id_lista=id_lista)

    return redirect('cria_lista:detalhe_lista', id_lista=id_lista)
