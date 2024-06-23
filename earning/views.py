from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from earning.models import Earning
from earning.forms import EarningForm


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class EarningRegisterView(generic.FormView):
    template_name = 'earning/registrar_ganhos.html'
    form_class = EarningForm
    success_url = reverse_lazy('earning:earning_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class EarningList(generic.ListView):
    model = Earning
    template_name = 'earning/ver_ganhos.html'
    context_object_name = 'earnings'

    def get_queryset(self):
        return Earning.objects.filter(user=self.request.user).order_by('-created_at')


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class EarningUpdate(generic.UpdateView):
    model = Earning
    template_name = 'earning/edit_ganhos.html'
    form_class = EarningForm
    context_object_name = 'earning'
    pk_url_kwarg = 'id_earning'

    def get_success_url(self):
        id_earning = self.kwargs['id_earning']
        return reverse('earning:earning_list')
