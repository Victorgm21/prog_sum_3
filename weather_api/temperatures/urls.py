from rest_framework.routers import DefaultRouter
from .views import cityTemperatureViewSet

router = DefaultRouter()
router.register(r'temperatures', cityTemperatureViewSet, basename='citytemperature')

urlpatterns = router.urls
