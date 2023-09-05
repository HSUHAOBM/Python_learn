from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from musics.views import MusicViewSet
from musics import views

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('musics', MusicViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]