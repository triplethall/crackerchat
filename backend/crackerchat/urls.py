from rest_framework.routers import DefaultRouter
from messaging.views import MessageViewSet

router = DefaultRouter()
router.register(r'posts', MessageViewSet, basename='post')
urlpatterns = router.urls
