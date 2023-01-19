import json
import random
from datetime import datetime

from asgiref.sync import async_to_sync

from message.models import Message
from service.models import Stations
import socket

class Rooms:
    def connect(self):
        stationList = Stations.objects.filter().all()
        for station in stationList:
            station.station_name
            WebSocket(
                'ws://'
                + socket.gethostname()
                + '/ws/chat/'
                + station.station_name
                + '/'
            )
