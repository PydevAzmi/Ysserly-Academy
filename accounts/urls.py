from django.urls import path, include
from .views import (
    FacebookLogin,
    GoogleLogin,
    GoogleRedirect,
    reset_password_confirm,
    email_confirmation
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('', include('dj_rest_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/account-confirm-email/<str:key>/', email_confirmation),

    path('password/reset/confirm/<uid>/<str:token>', reset_password_confirm, name="password_reset_confirm"),

    # social auth
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('google/callback/', GoogleRedirect.as_view(), name='google_redirect'),

]