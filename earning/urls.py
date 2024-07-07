from django.urls import path
from earning import views

app_name = 'earning'

urlpatterns = [
    path('registrar/', views.EarningRegisterView.as_view(), name='earning'),
    path('ganhos/', views.EarningList.as_view(), name='earning_list'),
    path('ganhos/editar/<int:id_earning>/', views.EarningUpdate.as_view(), name='earning_update'),
    path('ganhos/deletar/<int:id_earning>/', views.EarningDelete.as_view(), name='earning_delete'),
]
