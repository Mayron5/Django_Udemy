
from django.contrib import admin
from django.urls import path, include, re_path
from cursos.urls import router

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Django Alura')

urlpatterns = [
    re_path(r'^$', schema_view),
    path('api/v1/', include('cursos.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
