from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views.IndexView.as_view(), name="index")
    # path('/', admin.site.urls),
]
