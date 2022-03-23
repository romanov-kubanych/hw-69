from django.urls import path

from api_v1.views import echo_view

app_name = 'api_v1'


urlpatterns = [
    path('echo/', echo_view),
]
