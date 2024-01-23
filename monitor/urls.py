from django.urls import include, path

from monitor import views, views_partials

urlpatterns = [
    path("", views.maintenance, name="coming_soon"),
    path("index/", views.index, name="index"),


    # api access

    # partials
    path("partial/uptime", views_partials.node_uptime, name="partial_uptime"),
    path("partial/telemetry", views_partials.telemetry, name="partial_telemetry"),
    path("partial/block_count", views_partials.block_count, name="partial_block_count"),

]