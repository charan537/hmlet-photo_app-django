from django.urls import path
from .views import registration
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', registration, name='register'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]