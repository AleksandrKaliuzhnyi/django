from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # отслеживание переходов на определенную страницу
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
