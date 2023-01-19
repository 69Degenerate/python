from django.apps import AppConfig




class ServiceConfig(AppConfig):
    name = 'service'

    # def ready(self):
    #     # update my database here
    #     print("startUp")
    #     from service.rooms import Rooms
    #     Rooms.connect(Rooms)
    #     pass
