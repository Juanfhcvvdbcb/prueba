
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from Heavy_metal.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",  
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_drf/v1',include('api_drf.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('loginView/<str:username>/<str:password>/', login_view, name='login'),
    path('upload-image/', upload_image, name='upload_image'),
    path('upload-image-users/', upload_image, name='upload_image_users'),

   #Ruta del logueo con dos parametros
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


