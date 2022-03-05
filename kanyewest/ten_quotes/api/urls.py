from rest_framework import routers, urlpatterns
from .views import QuoteViewSet

router = routers.DefaultRouter()
router.register('api', QuoteViewSet, 'main')

urlpatterns = router.urls