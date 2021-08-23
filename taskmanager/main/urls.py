from django.urls import path
from . import views

urlpatterns = [
    # отслеживание переходов на определенную страницу
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
]
