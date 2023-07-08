import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth import logout

from chat.main import Chat
 
def home(request):
    if request.method == 'POST':
        if 'start_session' in request.POST:
            return redirect('logIn')
        elif 'close_session' in request.POST:
            logout(request)
            return redirect('logIn')
    else:
        if request.user.is_authenticated:
            historial=[
                {'id':'1','request':"Hola", 'response':"Hola, soy un chatbot"},
                {'id':'2','request':"Cuanto es -1*2300?", 'response':"-2300"},
                {'id':'3','request':"Eres real?", 'response':"Sí"},
            ]
            return render(request, 'chat.html', {'historial': historial})
        
        return redirect('logIn')
    
def delete(request):
    if request.method == "POST":
        data = request.POST.get('data')
        ids = json.loads(data)
        Chat.get_instance().delete_conversation(user=request.user , ids=ids)
        return JsonResponse({"result":"ok"})    

def message(request):
    if request.method == "POST":
        data = request.POST.get('data')
        message = json.loads(data)
        res = {"Respuesta del chat"} 
        return JsonResponse(res)
