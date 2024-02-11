from django.urls import include, path
from rest_framework import routers
from alquiler_patinetes import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'patinetes', views.PatineteViewSet)
router.register(r'alquileres', views.AlquilerViewSet)
router.register(r'usuarios', views.UsuarioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]

