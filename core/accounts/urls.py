from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.RegisterPage.as_view(), name="register"),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("", include("django.contrib.auth.urls")),
    path("send-email/", views.send_email, name="send-email"),
    path("test/", views.test, name="test"),
]
