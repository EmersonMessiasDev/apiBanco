from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from banco.api.viewsets import BancoViewSet

#? Rotas
router = routers.DefaultRouter()
router.register(r'banco', BancoViewSet)


#? Informações da API
schema_view = get_schema_view(
   openapi.Info(
      title="Projeto academico Api Banco",
      default_version='v.1',
      description="Api criada para uso na disciplina de testes unitario",
      terms_of_service="Criada para estudos",
      contact=openapi.Contact(email="emersonmessiasdev@gmail.com"),
      license=openapi.License(name="Liberada para estudos"),
   ),
   public=True,
)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    
    #? Gerar documentação automatica.
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
