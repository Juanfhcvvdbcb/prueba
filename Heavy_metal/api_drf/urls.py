from django.urls import path, include
from rest_framework import routers
from api_drf import views

router = routers.DefaultRouter()
router.register(r'Categorias', views.CategoriasViewSet)
router.register(r'Departamentos', views.DepartamentosViewSet)
router.register(r'Ciudades', views.CiudadesViewSet)
router.register(r'Estado', views.EstadoViewSet)
router.register(r'Marcas', views.MarcasViewSet)
router.register(r'medios_pago', views.medios_pagoViewSet)
router.register(r'Proveedores', views.ProveedoresViewSet)
router.register(r'Contactos', views.ContactosViewSet)
router.register(r'TipoIdentificacion', views.TipoIdentificacionViewSet)
router.register(r'Rol', views.RolViewSet)
router.register(r'Usuarios', views.UsuariosViewSet)
router.register(r'CarritoCompras', views.CarritoComprasViewSet)
router.register(r'Productos', views.ProductosViewSet)
router.register(r'ProveedoresProductos', views.ProveedoresProductosViewSet)
router.register(r'Comentarios', views.ComentariosViewSet)
router.register(r'Respuestas', views.RespuestasViewSet)
router.register(r'DetalleCarrito', views.DetalleCarritoViewSet)
router.register(r'Domicilios', views.DomiciliosViewSet)
router.register(r'ImagenesProducto', views.ImagenesProductoViewSet)
router.register(r'Ventas', views.VentasViewSet)


urlpatterns = [
    path('',include(router.urls)),
     path('upload-image/', views.upload_image, name='upload_image'),
]
