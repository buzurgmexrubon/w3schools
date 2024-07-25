from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.common.urls', namespace='common')),
    path('tutorials', include('apps.tutorials.urls', namespace='tutorials')),
    path('search/', include('apps.search.urls', namespace='search')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
