
from django.shortcuts import get_object_or_404

from chat.models import Historial


class Chat:
    __instance = None
    index = None
    query_engine = None
    def __init__(self):
        if Chat.__instance is not None:
            raise Exception("Singleton ya existe")
        else:
            Chat.__instance = self
        

    @staticmethod
    def get_instance():
        if Chat.__instance is None:
            Chat()
        return Chat.__instance
    
    def delete_conversation(self, user, ids):
        if(user.is_authenticated):    
            for id in ids:
                conversation = get_object_or_404(Historial, pk=id)
                conversation.delete()