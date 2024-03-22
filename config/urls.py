from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('InternoSai.urls')),
<<<<<<< HEAD
    path('home/', include('core.urls'))
    # path('accounts/', include('django.contrib.auth.urls')),
=======
    path('accounts/', include('django.contrib.auth.urls')),
>>>>>>> 6133edad35565e743e5168cdd11cb9588b2c5eba
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)