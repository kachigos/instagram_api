from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cart.views import CartApiView
from rest_auth.views import PasswordResetConfirmView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title = 'INSTAGRAM API',
        description = 'URLки  instagram',
        default_version = 'v1',
    ),
    public = True
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/post/', include('post.urls')),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/follow/', include('follow.urls')),
    path('api/v1/cart/', CartApiView.as_view()),
    path('docs/', schema_view.with_ui('swagger')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

