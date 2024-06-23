from django.urls import path
from earning import views

app_name = 'earning'

urlpatterns = [
    path('registrar-ganhos/', views.EarningRegisterView.as_view(), name='earning'),
    path('ver-ganhos/', views.EarningList.as_view(), name='earning_list'),
    path('ganhos/editar-ganhos/<int:id_earning>/', views.EarningUpdate.as_view(), name='earning_update'),
]
