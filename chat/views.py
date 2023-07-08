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
            historial=Chat.get_instance().load_chat(request.user)
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
        data = request.POST.get('req')
        d = Chat.get_instance().response(request.user,data)
        return JsonResponse(d)
