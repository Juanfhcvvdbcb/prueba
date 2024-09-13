from rest_framework import serializers

from .models import Categorias, Departamentos, Ciudades, Estado, Marcas, MediosPago, Proveedores, Contactos, TipoIdentificacion, Rol, Usuarios, CarritoCompras, Productos, ProveedoresProductos, Comentarios, Respuestas,  DetalleCarrito, Domicilios, ImagenesProducto, Ventas

class CategoriasSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class DepartamentosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'


class CiudadesSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = '__all__'

class EstadoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class MarcasSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'


class medios_pagoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = MediosPago
        fields = '__all__'                               

class ProveedoresSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'


class ContactosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = '__all__'


class TipoIdentificacionSerializaer(serializers.ModelSerializer):
    class Meta:
        model = TipoIdentificacion
        fields = '__all__'

class RolSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuariosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class CarritoComprasSerializaer(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'

class ProductosSerializaer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(source='marca.nombre_marca', read_only=True)
    nombre_marca = serializers.IntegerField(source='detalle_carrito.cantidad', read_only=True)
    class Meta:
        model = Productos
        fields = ['codigo', 'nombre_producto', 'precio', 'nombre_marca', 'marca', 'categoria']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ajusta la representación para enviar los IDs en lugar de los objetos completos
        representation['marca'] = instance.marca.id if instance.marca else None
        representation['categoria'] = instance.categoria.id if instance.categoria else None
        return representation


class ProveedoresProductosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresProductos
        fields = '__all__'

class ComentariosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

class RespuestasSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Respuestas
        fields = '__all__'



class DetalleCarritoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCarrito
        fields = '__all__'

class DomiciliosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Domicilios
        fields = '__all__'

class ImagenesProductoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesProducto
        fields = '__all__'

class VentasSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'