from rest_framework import routers
from .views import PostView

router = routers.DefaultRouter()
router.register('posts', PostView)

urlpatterns = router.urls
