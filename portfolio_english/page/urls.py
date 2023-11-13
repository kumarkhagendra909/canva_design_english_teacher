# url for the page app 
from django.urls import path

from .views import home
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('', home, name = "home"),
]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
