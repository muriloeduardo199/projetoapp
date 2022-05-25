
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include('applocalizacao.urls',namespace="pages")),
    path('admin/', admin.site.urls),
   
]
