from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "", auth_views.LoginView.as_view(), name="login"
    ),  # Redirige la URL raíz a la vista de inicio de sesión
    path("auth/", include("autenticacion.urls")),
    path("inicio/", include("inicio.urls")),
    path("buscador/", include("buscador.urls")),
    path("departamentos/", include("departamentos.urls")),
    path("unidadesmd/", include("unidadesmd.urls")),
    path("matriz_dispositivos/", include("matriz_dispositivos.urls")),
    path("listado_dispositivos_medicos/", include("listado_dispositivos_medicos.urls")),
    path("matriz_medicamentos/", include("matriz_medicamentos.urls")),
    path("importacion/", include("importacion.urls")),
    path("priorizacion/", include("priorizacion.urls")),
    path("backup_manager/", include("backup_manager.urls")),
    path("user_profiles/", include("user_profiles.urls")),
    path("admin/", admin.site.urls),
]

# Si el proyecto está en modo DEBUG (desarrollo), entonces sirve los archivos media.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
