from rest_framework import routers
from apps.views import ObjectViewSet

router = routers.DefaultRouter()
router.register('objects', ObjectViewSet)
