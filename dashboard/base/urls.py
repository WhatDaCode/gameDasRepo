from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='base-about')
    # path('accounts/', views.accounts, name="accounts")
]