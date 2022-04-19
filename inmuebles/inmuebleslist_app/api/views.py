from rest_framework.response import Response
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class InmuebleListAV(APIView):
    
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = InmuebleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class InmuebleDetalleAV(APIView):
    def get(self,request,x):
        try:
            inmueble=Inmueble.objects.get(pk=x)
        except Inmueble.DoesNotExist:
            return Response({'error':'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    
    def put(self,request,x):
        try:
            inmueble=Inmueble.objects.get(pk=x)
        except Inmueble.DoesNotExist:
            return Response({'error':'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InmuebleSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,x):
        try:
            inmueble=Inmueble.objects.get(pk=x)
        except Inmueble.DoesNotExist:
            return Response({'error':'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# @api_view(['GET','POST'])#Este decorador cuando no tiene nada es un GET
# def inmuebles_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         #La siguiente linea serializa toda la data
#         serializer = InmuebleSerializer(inmuebles, many = True)#many quiere decir q son muchos los vaores a devolver
#         return Response(serializer.data)#devuelve e Json
  
    
#     if request.method == 'POST':
#         de_serializar = InmuebleSerializer(data=request.data)
#         if de_serializar.is_valid():
#             de_serializar.save()
#             return Response(de_serializar.data)
#         else:
#             return Response(de_serializar.errors)
            

# @api_view(['GET','PUT','DELETE'])#Este decorador cuando no tiene nada es un GET
# def inmueble_detalle(request, x):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=x)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'Error':'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=x)
#         de_serializar = InmuebleSerializer(inmueble,data=request.data)
#         if de_serializar.is_valid():
#             de_serializar.save()
#             return Response(de_serializar.data)
#         else:
#             return Response(de_serializar.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk=x)
#             inmueble.delete()
#         except Inmueble.DoesNotExist:
#             return Response({'Error':'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        
#         return Response(status=status.HTTP_204_NO_CONTENT)

