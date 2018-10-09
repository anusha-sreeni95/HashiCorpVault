from django.conf.urls import url, include
from .views import LoginView
from .utils import logout_view

urlpatterns = [
  url("^login$", LoginView.as_view(), name="loginview"),
  url("^logout$", logout_view, name="logoutview"),
]