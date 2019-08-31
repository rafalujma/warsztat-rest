from django.contrib import admin
from django.urls import path

from api.views import (
    PersonListView,
    PersonDetailView,
    MovieListView,
    MovieDetailView,
    LoginView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("persons/", PersonListView.as_view(), name="person-list"),
    path("persons/<int:pk>/", PersonDetailView.as_view(), name="person-detail"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("login/", LoginView.as_view(), name="login"),
]
