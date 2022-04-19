from django.urls import path
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetalleAV, EmpresaAV, EmpresaDetalleAV

urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:x>', InmuebleDetalleAV.as_view(), name='inmueble-detail'),
    path('empresas/', EmpresaAV.as_view(), name='empresa'),
    path('empresas/<int:x>', EmpresaDetalleAV.as_view(), name='empresa-detail'),

]