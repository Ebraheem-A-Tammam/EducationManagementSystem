from django.urls import path

from .views import (
    article_list_view,
    article_detail_view,
    article_create_view,
    article_update_view,
)

app_name = "forums"

urlpatterns = [
    path("", article_list_view, name="article_list"),
    path("create/", article_create_view, name="article_create"),
    path("<int:article_id>/edit/", article_update_view, name="article_update"),
    path("<int:article_id>/", article_detail_view, name="article_detail"),
]
