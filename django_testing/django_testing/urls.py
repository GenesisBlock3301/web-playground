
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Auth.views import UserRegistrationViewset, UserViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewset,basename="users")
router.register(r'register',UserRegistrationViewset,basename="register")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("",include("app.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
