from django.db.models import Max
from rest_framework import viewsets,  status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Categorias, Departamentos, Ciudades, Estado, Marcas, MediosPago, Proveedores, Contactos, TipoIdentificacion, Rol, Usuarios, CarritoCompras, Productos, ProveedoresProductos, Comentarios, Respuestas, DetalleCarrito, Domicilios, ImagenesProducto, Ventas
from .serializer import CategoriasSerializaer, DepartamentosSerializaer, CiudadesSerializaer, EstadoSerializaer, MarcasSerializaer, medios_pagoSerializaer, ProveedoresSerializaer, ContactosSerializaer, TipoIdentificacionSerializaer, RolSerializaer, UsuariosSerializaer, CarritoComprasSerializaer, ProductosSerializaer, ProveedoresProductosSerializaer, ComentariosSerializaer, RespuestasSerializaer, DetalleCarritoSerializaer, DomiciliosSerializaer, ImagenesProductoSerializaer, VentasSerializaer
from django.contrib.auth.hashers import check_password 
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError 
from django.db.models import Sum

@api_view(['POST'])
def upload_image(request):
    files = request.FILES.getlist('image')
    print('Archivos recibidos:', files)
    for file in files:
        path = default_storage.save(f'media/productos/{file.name}', ContentFile(file.read()))
        print(f'Archivo guardado en: {path}')
    return Response({"message": "Images uploaded successfully"}, status=status.HTTP_201_CREATED)
    
class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializaer

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializaer

class CiudadesViewSet(viewsets.ModelViewSet):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializaer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializaer

class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializaer

class medios_pagoViewSet(viewsets.ModelViewSet):
    queryset = MediosPago.objects.all()
    serializer_class = medios_pagoSerializaer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializaer

class ContactosViewSet(viewsets.ModelViewSet):
    queryset = Contactos.objects.all()
    serializer_class = ContactosSerializaer


class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIdentificacion.objects.all()
    serializer_class = TipoIdentificacionSerializaer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializaer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializaer

    def retrieve(self, request, *args, **kwargs):
        print('Datos recibidos para obtener usuario:', kwargs)
        response = super().retrieve(request, *args, **kwargs)
        print('Datos enviados del usuario:', response.data)
        return response
        
    def create(self, request, *args, **kwargs):
        print('Datos recibidos en el servidor:', request.data)
        print('Archivos recibidos:', request.FILES)
        
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            print('Datos enviados al cliente:', serializer.data)
            
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            print('Response:', response.data)
            return response
        except ValidationError as e:
            valid_data = {field: value for field, value in request.data.items() if field not in e.detail}
            invalid_data = {field: value for field, value in request.data.items() if field in e.detail}
            
            print('Campos válidos:', valid_data)
            print('Campos con errores:', invalid_data)
            
            return Response({
                'detail': 'Error de validación',
                'errors': e.detail,
                'valid_data': valid_data,
                'invalid_data': invalid_data
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error inesperado:', str(e))
            return Response({
                'detail': 'Error inesperado',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                



    @action(detail=False, methods=['post'], url_path='authenticate')
    def authenticate_user(self, request):
        id_usuario = request.data.get('id_usuario')
        contraseña = request.data.get('Contraseña_Encriptada')

        print('Datos recibidos:', request.data)

        if id_usuario is None or contraseña is None:
            print('ID de usuario y contraseña son requeridos.')
            return Response({'detail': 'ID de usuario y contraseña son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuarios.objects.get(id_usuario=id_usuario)
        except Usuarios.DoesNotExist:
            print('Usuario no encontrado.')
            return Response({'detail': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        # Comparar la contraseña directamente
        if usuario.Contraseña_Encriptada != contraseña:
            print('Credenciales inválidas.')
            return Response({'detail': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

        print('Autenticación exitosa.')
        return Response({'detail': 'OK'}, status=status.HTTP_200_OK)




class CarritoComprasViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompras.objects.all()
    serializer_class = CarritoComprasSerializaer

    @action(detail=True, methods=['get'], url_path='carrito-usuario')
    def productos(self, request, pk=None):
        print(f"Solicitud recibida con ID de carrito: {pk}")
        try:
            detalle_carrito = DetalleCarrito.objects.filter(id_carrito=pk).select_related('id_producto__marca')
            productos = [detalle.id_producto for detalle in detalle_carrito]
            serializer = ProductosSerializaer(productos, many=True)
            print(f"Productos obtenidos: {serializer.data}")
            return Response(serializer.data)
        except DetalleCarrito.DoesNotExist:
            print("Carrito no encontrado")
            return Response({"error": "Carrito no encontrado"}, status=404)

    @action(detail=False, methods=['get'], url_path='id-carrito')
    def id_carrito(self, request):
        id_usuario = request.query_params.get('id_usuario')

        if not id_usuario:
            response = {"error": "id_usuario is required"}
            print(response)
            return Response({"error": "id_usuario is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verificar si existe algún carrito con estado activo (estado_carrito=1) para el usuario dado
            carrito = CarritoCompras.objects.filter(id_usuario=id_usuario, estado_carrito=1).first()
        except CarritoCompras.DoesNotExist:
            response = {"message": "No se encontraron carritos para el usuario dado"}
            print(response)
            return Response({"message": "No se encontraron carritos para el usuario dado"}, status=status.HTTP_404_NOT_FOUND)

        if carrito:
            response = {"id_carrito": carrito.id_carrito}
            print(response)
            return Response({"id_carrito": carrito.id_carrito}, status=status.HTTP_200_OK)
        else:
            response = {"id_carrito": 0}
            print(response)
            return Response({"id_carrito": 0}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='buscar-productos')
    def busca_carrito_activo(self, request):
        id_usuario = request.query_params.get('id_usuario')
        id_carrito = request.query_params.get('id_carrito')
        estado_activo = 1  # Asumiendo que el estado activo tiene el id 1
        
        if not id_usuario or not id_carrito:
            return Response({"error": "id_usuario and id_carrito are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filtra los productos que cumplen ciertas condiciones
        productos = Productos.objects.filter(
            detallecarrito__id_carrito__id_carrito=id_carrito,
            detallecarrito__id_carrito__id_usuario=id_usuario,
            detallecarrito__id_carrito__estado_carrito=estado_activo
        ).select_related('marca').values(
            'nombre_producto', 'marca__nombre_marca', 'precio', 'detallecarrito__cantidad'
        )
        
        # Imprimir en terminal para depuración
        print(f"Productos encontrados para id_usuario={id_usuario} y id_carrito={id_carrito}: {productos}")
        
        if productos:
            return Response({"id_carrito": id_carrito}, status=status.HTTP_200_OK)
        else:
            return Response({"id_carrito": 0}, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'], url_path='ultimo-id')
    def obtener_ultimo_id(self, request):
        try:
            ultimo_id = CarritoCompras.objects.latest('id_carrito').id_carrito + 1
        except CarritoCompras.DoesNotExist:
            ultimo_id = 1  # Si no hay ningún carrito, empezamos desde el ID 1
        
        return Response({"ultimo_id": ultimo_id}, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['get'], url_path='valida-estado')
    def valida_estado(self, request):
        id_usuario = request.query_params.get('id_usuario')

        if not id_usuario:
            response = {"error": "id_usuario is required"}
            print(response) 
            return Response({"error": "id_usuario is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verificar si existe algún estado activo (estado_carrito=1) para el usuario dado
            tiene_carro_activo = CarritoCompras.objects.filter(id_usuario=id_usuario, estado_carrito=1).exists()
        except CarritoCompras.DoesNotExist:
            response = {"message": "No se encontraron carritos para el usuario dado"}
            print(response) 
            return Response({"message": "No se encontraron carritos para el usuario dado"}, status=status.HTTP_404_NOT_FOUND)

        if tiene_carro_activo:
            response = {"mensaje": "Tiene carro activo"}
            print(response) 
            return Response({"mensaje": "Tiene carro activo"}, status=status.HTTP_200_OK)
        else:
            response = {"mensaje": "Es procedente insertar carrito"}
            print(response) 
            return Response({"mensaje": "Es procedente insertar carrito"}, status=status.HTTP_200_OK)


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializaer

    def create(self, request, *args, **kwargs):
        print('Datos recibidos en el servidor:', request.data)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        print('Datos enviados al cliente:', serializer.data)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'], url_path='busq-filtro-prod')
    def buscar_por_nombre(self, request):
        nombre_producto = request.query_params.get('nombre', None)
        if nombre_producto is not None:
            productos = Productos.objects.filter(nombre_producto__icontains=nombre_producto)
            serializer = self.get_serializer(productos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Nombre de producto no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='busq-filtro-prod')
    def buscar_por_filtros(self, request):
        precio_menor = request.query_params.get('precio_menor', None)
        precio_mayor = request.query_params.get('precio_mayor', None)
        categoria_id = request.query_params.get('categoria_id', None)
        marca_id = request.query_params.get('marca_id', None)

        filtros = {}
        if precio_menor:
            filtros['precio__gte'] = precio_menor
        if precio_mayor:
            filtros['precio__lte'] = precio_mayor
        if categoria_id and categoria_id != '0':
            filtros['categoria_id'] = categoria_id
        if marca_id and marca_id != '0':
            filtros['marca_id'] = marca_id

        productos = Productos.objects.filter(**filtros)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProveedoresProductosViewSet(viewsets.ModelViewSet):
    queryset = ProveedoresProductos.objects.all()
    serializer_class = ProveedoresProductosSerializaer


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializaer

class RespuestasViewSet(viewsets.ModelViewSet):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializaer


class DetalleCarritoViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializaer

    def create(self, request, *args, **kwargs):
        print("Datos recibidos en el servidor:", request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("Datos validados correctamente:", serializer.validated_data)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            print("Respuesta enviada al cliente:", response.data)
            return response
        else:
            print("Errores de validación:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_path='ultimo-id-carrito')
    def obtener_ultimo_id(self, request):
        try:
            ultimo_id_det = DetalleCarrito.objects.latest('id_detalle').id_detalle + 1
        except DetalleCarrito.DoesNotExist:
            ultimo_id_det = 1  # Si no hay ningún detalle carrito, empezamos desde el ID 1
        
        # Imprimir en la terminal el ID obtenido
        print(f"Último ID de detalle carrito obtenido: {ultimo_id_det}")

        return Response({"ultimo_id_det": ultimo_id_det}, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'], url_path='suma-total-productos')
    def obtener_suma_total_productos(self, request):
        id_carrito = request.query_params.get('idCarrito')
        user_id = request.query_params.get('userId')

        # Imprimir los valores recibidos
        print(f"ID Carrito recibido: {id_carrito}")
        print(f"ID Usuario recibido: {user_id}")

        try:
            suma_total_productos = DetalleCarrito.objects.filter(
                id_carrito__id_carrito=id_carrito,
                id_carrito__id_usuario=user_id
            ).aggregate(Sum('total_productos'))['total_productos__sum'] or 0

            # Imprimir el resultado de la consulta
            print(f"Suma total de productos: {suma_total_productos}")

            return Response({"suma_total_productos": suma_total_productos}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error al obtener la suma total de productos: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='detalle-carrito')
    def detalle_carrito(self, request):
        id_carrito = request.query_params.get('id_carrito')
        id_producto = request.query_params.get('id_producto')

        print(f"Recibido id_carrito: {id_carrito}, id_producto: {id_producto}")

        if not id_carrito or not id_producto:
            return Response({"error": "id_carrito and id_producto are required"}, status=status.HTTP_400_BAD_REQUEST)

        detalles = DetalleCarrito.objects.filter(id_carrito=id_carrito, id_producto=id_producto)
        serializer = DetalleCarritoSerializaer(detalles, many=True)
        
        print(f"Enviando datos serializados: {serializer.data}")
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='verifica-producto')
    def verifica_producto(self, request):
        id_carrito = request.query_params.get('id_carrito')
        id_producto = request.query_params.get('id_producto')

        if not id_carrito or not id_producto:
            return Response({"error": "id_carrito and id_producto are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            count = DetalleCarrito.objects.filter(id_carrito=id_carrito, id_producto=id_producto).count()
        except DetalleCarrito.DoesNotExist:
            return Response({"count": 0}, status=status.HTTP_200_OK)

        if count > 0:
            return Response({"count": count}, status=status.HTTP_200_OK)
        else:
            return Response({"count": 0}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='update-cantidad')
    def update_cantidad(self, request):
        id_detalle = request.data.get('ID_Detalle')
        id_carrito = request.data.get('ID_Carrito')
        id_producto = request.data.get('ID_Producto')
        nueva_cantidad = request.data.get('Cantidad')

        if not id_detalle or not id_carrito or not id_producto or nueva_cantidad is None:
            return Response({"error": "ID_Detalle, ID_Carrito, ID_Producto, and Cantidad are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            detalle_carrito = DetalleCarrito.objects.get(id=id_detalle, id_carrito=id_carrito, id_producto=id_producto)
            detalle_carrito.Cantidad = nueva_cantidad
            detalle_carrito.save()
            serializer = DetalleCarritoSerializaer(detalle_carrito)

            # Preparar los datos de respuesta
            response_data = {
                "ID_Detalle": detalle_carrito.id,
                "ID_Carrito": detalle_carrito.id_carrito,
                "ID_Producto": detalle_carrito.id_producto,
                "Cantidad": detalle_carrito.Cantidad,
                "Total_Productos": detalle_carrito.total_productos
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except DetalleCarrito.DoesNotExist:
            return Response({"error": "DetalleCarrito not found"}, status=status.HTTP_404_NOT_FOUND)

class DomiciliosViewSet(viewsets.ModelViewSet):
    queryset = Domicilios.objects.all()
    serializer_class = DomiciliosSerializaer

    def create(self, request, *args, **kwargs):
        print('Datos recibidos en el servidor:', request.data)
        print('Archivos recibidos:', request.FILES)
        
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            print('Datos enviados al cliente:', serializer.data)
            
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            print('Response:', response.data)
            return response
        except ValidationError as e:
            valid_data = {field: value for field, value in request.data.items() if field not in e.detail}
            invalid_data = {field: value for field, value in request.data.items() if field in e.detail}
            
            print('Campos válidos:', valid_data)
            print('Campos con errores:', invalid_data)
            
            return Response({
                'detail': 'Error de validación',
                'errors': e.detail,
                'valid_data': valid_data,
                'invalid_data': invalid_data
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error inesperado:', str(e))
            return Response({
                'detail': 'Error inesperado',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImagenesProductoViewSet(viewsets.ModelViewSet):
    queryset = ImagenesProducto.objects.all()
    serializer_class = ImagenesProductoSerializaer

    def list(self, request, *args, **kwargs):
        id_producto = request.query_params.get('id_producto', None)
        print(f"Solicitud recibida con id_producto: {id_producto}")

        if id_producto is None:
            print("id_producto no proporcionado")
            return Response({"error": "id_producto no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset().filter(id_producto=id_producto))
        print(f"Queryset filtrado: {queryset}")

        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data

        print(f"Datos enviados al cliente: {response_data}")
        return Response(response_data, status=status.HTTP_200_OK)
class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializaer

    def create(self, request, *args, **kwargs):
        print('Datos recibidos en el servidor:', request.data)
        print('Archivos recibidos:', request.FILES)
        
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            print('Datos enviados al cliente:', serializer.data)
            
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            print('Response:', response.data)
            return response
        except ValidationError as e:
            valid_data = {field: value for field, value in request.data.items() if field not in e.detail}
            invalid_data = {field: value for field, value in request.data.items() if field in e.detail}
            
            print('Campos válidos:', valid_data)
            print('Campos con errores:', invalid_data)
            
            return Response({
                'detail': 'Error de validación',
                'errors': e.detail,
                'valid_data': valid_data,
                'invalid_data': invalid_data
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error inesperado:', str(e))
            return Response({
                'detail': 'Error inesperado',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


