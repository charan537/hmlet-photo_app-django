from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="Photo API")

router = routers.DefaultRouter()
router.register(r'myphotos', views.PhotosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('photoApi/', include(router.urls)),
    path('photoApi/photoList', views.PhotoListView.as_view(),name='photoList'),
    path('photoApi/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('photoApi/jwtauth/', include('jwtauth.urls'), name='jwtauth'),
    path('photoApi/docs/', schema_view), 
]