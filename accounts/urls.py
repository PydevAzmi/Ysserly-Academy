from django.urls import path, include
from .views import (
    FacebookLogin,
    GoogleLogin,
    GoogleRedirect,
    reset_password_confirm,
    email_confirmation
    )
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView


urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('', include('dj_rest_auth.urls')),
    path('registration/account-confirm-email/<str:key>/', VerifyEmailView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('password/reset/confirm/<uid>/<str:token>', reset_password_confirm, name="password_reset_confirm"),

    # social auth
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('google/callback/', GoogleRedirect.as_view(), name='google_redirect'),

]