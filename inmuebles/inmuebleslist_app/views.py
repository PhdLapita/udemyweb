# from django.shortcuts import render
# from inmuebleslist_app.models import Inmueble
# from django.http import JsonResponse
# # Create your views here.
# def inmueble_list(request):
#     inmuebles = Inmueble.objects.all()
#     data ={
#         'inmuebles': list(inmuebles.values()),
#     }
    
#     return JsonResponse(data)

# def inmueble_detalle(request,x):
#     inmueble = Inmueble.objects.get(pk=x)
#     data = {
#         'direccion': inmueble.direccion,
#         'pais': inmueble.pais,
#         'imagen': inmueble.imagen,
#         'activo': inmueble.active,
#         'direccion': inmueble.descripcion,        
#     }
#     return JsonResponse(data)