from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
#from rest_framework.documentation import include_docs_urls
#from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('accounts.urls')),
    #path('docs/', include_docs_urls(title='My API Docs')),
    #path('docs/', get_swagger_view(title='My API Docs')),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings. MEDIA_URL, document_root = settings.MEDIA_ROOT)