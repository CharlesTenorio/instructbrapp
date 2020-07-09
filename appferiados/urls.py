from django.contrib import admin
from django.urls import path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls import include
from cidades.api.viewsets import CidadeViewSet
from cidades.api.viewsets import UfViewSet
from cidades.api.views import CarregaCidadesAPIView
from feriados.api.viewsets import FeraiadoUFViewSet
from feriados.api.viewsets import FeriadoMunicipalViewSet
from feriados.api.views import FeriadoConsultarAPIView


schema_view = get_schema_view(
   openapi.Info(
      title="Instruct Feriados API",
      default_version='v1',
      description="Documentacao APIS",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

router = routers.SimpleRouter()
router.register(r'api/uf', CidadeViewSet)
router.register(r'api/cidade', UfViewSet)
router.register(r'api/feraidos/estadual', FeraiadoUFViewSet)
router.register(r'api/feraidos/municipal', FeriadoMunicipalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/cidade/importar', CarregaCidadesAPIView.as_view(), name='importar'),
    path('feriados/<str:codigo>/<str:data_feriado>/', FeriadoConsultarAPIView.as_view(), name='feriados'),

]