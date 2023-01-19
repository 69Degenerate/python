from django.conf.urls import url

from distribute.consumer import  StationConsumer

websocket_urlpatterns = [

    url('ws/section/<int:room_id>/', StationConsumer.as_asgi()),

]