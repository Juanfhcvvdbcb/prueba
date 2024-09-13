# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CarritoCompras(models.Model):
    id_carrito = models.IntegerField(db_column='ID_Carrito', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ID_Usuario', blank=True, null=True)  # Field name made lowercase.
    estado_carrito = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_carrito', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrito_compras'


class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Ciudades(models.Model):
    id_ciudad = models.IntegerField(db_column='ID_Ciudad', primary_key=True)  # Field name made lowercase.
    nombre_ciudad = models.CharField(max_length=100, blank=True, null=True)
    id_departamento = models.ForeignKey('Departamentos', models.DO_NOTHING, db_column='ID_Departamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudades'


class Comentarios(models.Model):
    id_comentario = models.IntegerField(db_column='ID_Comentario', primary_key=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ID_Usuario', blank=True, null=True)  # Field name made lowercase.
    codigo_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='Codigo_Producto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comentarios'


class Contactos(models.Model):
    num_identificacion = models.IntegerField(db_column='NUM_IDENTIFICACION', primary_key=True)  # Field name made lowercase.
    tipo = models.ForeignKey('TipoIdentificacion', models.DO_NOTHING, db_column='TIPO_ID', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='PROVEEDOR', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contactos'


class Departamentos(models.Model):
    id_departamento = models.IntegerField(db_column='ID_Departamento', primary_key=True)  # Field name made lowercase.
    nombre_departamento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class DetalleCarrito(models.Model):
    id_detalle = models.IntegerField(db_column='ID_Detalle', primary_key=True)  # Field name made lowercase.
    id_carrito = models.ForeignKey(CarritoCompras, models.DO_NOTHING, db_column='ID_Carrito', blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_Producto', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    total_productos = models.IntegerField(db_column='Total_Productos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_carrito'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Domicilios(models.Model):
    id_domicilio = models.IntegerField(db_column='ID_Domicilio', primary_key=True)  # Field name made lowercase.
    id_detallecompra = models.ForeignKey(DetalleCarrito, models.DO_NOTHING, db_column='ID_DetalleCompra', blank=True, null=True)  # Field name made lowercase.
    valor_domicilio = models.DecimalField(db_column='Valor_Domicilio', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='ID_Estado', blank=True, null=True)  # Field name made lowercase.
    fecha_entrega = models.DateTimeField(db_column='Fecha_Entrega')  # Field name made lowercase.
    observaciones_domiciliario = models.TextField(db_column='Observaciones_Domiciliario', blank=True, null=True)  # Field name made lowercase.
    observaciones_cliente = models.TextField(db_column='Observaciones_Cliente', blank=True, null=True)  # Field name made lowercase.
    calificacion = models.IntegerField(db_column='Calificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'domicilios'


class Estado(models.Model):
    id_estado = models.IntegerField(db_column='ID_Estado', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'


class GestionarproductosCategorias(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestionarproductos_categorias'


class GestionarproductosImagenesproducto(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('GestionarproductosProductos', models.DO_NOTHING, db_column='ID_Producto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gestionarproductos_imagenesproducto'


class GestionarproductosMarcas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestionarproductos_marcas'


class GestionarproductosProductos(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    stock = models.IntegerField(blank=True, null=True)
    descripcion_producto = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    categoria = models.ForeignKey(GestionarproductosCategorias, models.DO_NOTHING, blank=True, null=True)
    marca = models.ForeignKey(GestionarproductosMarcas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestionarproductos_productos'


class GestionusuariosUsuarios(models.Model):
    id_usuario = models.IntegerField(db_column='ID_Usuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correo_electronico = models.CharField(db_column='Correo_Electronico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    Contraseña_Encriptada = models.CharField(db_column='Contrase▒a_Encriptada', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_ciudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='ID_Ciudad', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='ID_Estado', blank=True, null=True)  # Field name made lowercase.
    id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='ID_Rol', blank=True, null=True)  # Field name made lowercase.
    tipo_identificacion = models.ForeignKey('TipoIdentificacion', models.DO_NOTHING, db_column='Tipo_Identificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gestionusuarios_usuarios'


class ImagenesProducto(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_Producto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagenes_producto'


class IndexUsuarios(models.Model):
    id_usuario = models.IntegerField(db_column='ID_Usuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correo_electronico = models.CharField(db_column='Correo_Electronico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    Contraseña_Encriptada = models.CharField(db_column='Contraseña_Encriptada', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_ciudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='ID_Ciudad', blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='ID_Estado', blank=True, null=True)  # Field name made lowercase.
    id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='ID_Rol', blank=True, null=True)  # Field name made lowercase.
    tipo_identificacion = models.ForeignKey('TipoIdentificacion', models.DO_NOTHING, db_column='Tipo_Identificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'index_usuarios'


class Marcas(models.Model):
    nombre_marca = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'


class MediosPago(models.Model):
    id_mediopago = models.IntegerField(db_column='ID_MedioPago', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medios_pago'


class Productos(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    stock = models.IntegerField(blank=True, null=True)
    descripcion_producto = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    marca = models.ForeignKey(Marcas, models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    nit = models.IntegerField(db_column='NIT', primary_key=True)  # Field name made lowercase.
    razon_social = models.CharField(db_column='RAZON_SOCIAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedores'


class ProveedoresProductos(models.Model):
    proveedor = models.OneToOneField(Proveedores, models.DO_NOTHING, db_column='PROVEEDOR', primary_key=True)  # Field name made lowercase. The composite primary key (PROVEEDOR, PRODUCTO) found, that is not supported. The first column is selected.
    producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='PRODUCTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedores_productos'
        unique_together = (('proveedor', 'producto'),)


class Respuestas(models.Model):
    id_respuesta = models.IntegerField(db_column='ID_Respuesta', primary_key=True)  # Field name made lowercase.
    respuesta = models.TextField(db_column='Respuesta', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ID_Usuario', blank=True, null=True)  # Field name made lowercase.
    id_comentario = models.ForeignKey(Comentarios, models.DO_NOTHING, db_column='ID_Comentario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'respuestas'


class Rol(models.Model):
    id_rol = models.IntegerField(db_column='ID_Rol', primary_key=True)  # Field name made lowercase.
    nombre_rol = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class TipoIdentificacion(models.Model):
    id_tipo = models.IntegerField(db_column='ID_Tipo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_identificacion'


class Usuarios(models.Model):
    id_usuario = models.IntegerField(db_column='ID_Usuario', primary_key=True)  # Field name made lowercase.
    nombre_usuario = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correo_electronico = models.CharField(db_column='Correo_Electronico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    Contraseña_Encriptada = models.CharField(db_column='Contraseña_Encriptada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='ID_Estado', blank=True, null=True)  # Field name made lowercase.
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='ID_Rol', blank=True, null=True)  # Field name made lowercase.
    id_ciudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='ID_Ciudad', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, models.DO_NOTHING, db_column='Tipo_Identificacion', blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'


class Ventas(models.Model):
    id_venta = models.IntegerField(db_column='ID_Venta', primary_key=True)  # Field name made lowercase.
    id_domicilio = models.ForeignKey(Domicilios, models.DO_NOTHING, db_column='ID_Domicilio', blank=True, null=True)  # Field name made lowercase.
    total_compra = models.DecimalField(db_column='Total_Compra', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_mediopago = models.ForeignKey(MediosPago, models.DO_NOTHING, db_column='ID_MedioPago', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ventas'
