
import os
import sys
from django.shortcuts import get_object_or_404
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import openai
from chat.models import Historial
from prepare_data import prepare_data

API_KEY= "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"
model_id = 'gpt-3.5-turbo'
class Chat:
    __instance = None
    index=None
    query_engine = None
    def __init__(self):
        if Chat.__instance is not None:
            raise Exception("Singleton ya existe")
        else:
            Chat.__instance = self
        openai.api_key = API_KEY
        os.environ['OPENAI_API_KEY'] = API_KEY
        prepare_data()
        self.indexing_data()

    @staticmethod
    def get_instance():
        if Chat.__instance is None:
            Chat()
        return Chat.__instance
    
    def response(self, user, req):
        try:
            res = self.query_engine.query(req)
            msg = res.response
            print("res: ",res.response)
            print("req: ",req)
        except Exception:
            msg="Ocurrió un error"
            historial={'req':req,'res':msg}
            return {"id":"0","data":historial}
        
        historial={'req':req,'res':msg}
        id = self.save_historial(user, historial)
        return {"id":id,"data":historial}
    
    def save_historial(self, user, historial):
        id = "0"
        if(user.is_authenticated):
            chat = Historial(user=user, request=historial['req'], response=historial['res'])
            chat.save()
            id = chat.id 
        return id

    def load_chat(self, user):
        if(user.is_authenticated):
            return Historial.objects.filter(user=user)
        else:
            return []
        
    def delete_conversation(self, user, ids):
        if(user.is_authenticated):    
            for id in ids:
                conversation = get_object_or_404(Historial, pk=id)
                conversation.delete()

    def indexing_data(self):
        print("Indexando datos...")
        try:
            docs = SimpleDirectoryReader(input_files=["./data/armas.txt"]).load_data()
            self.index = GPTVectorStoreIndex.from_documents(docs)
            self.query_engine = self.index.as_query_engine()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(f"Caught exception: {exc_type}: {exc_value}")