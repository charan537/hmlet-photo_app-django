from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'photos', views.PhotosViewSet)
#router.register(r'myphotos', views.MyPhotosViewSet,basename='Photo')
#router.register(r'mydrafts', views.MyDraftPhotosViewSet,basename='Photo')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('photoApi/', include(router.urls)),
    path('photoApi/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('photoApi/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('photoApi/auth/', include('rest_framework.urls', namespace='rest_framework'))
]