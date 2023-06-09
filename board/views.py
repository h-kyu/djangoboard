from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import BoardModel
# Create your views here.

def index(request):
    return render(request, 'board/index.html')

def list(request):
    board_list = BoardModel.objects.all()
    return render(
        request,
        'board/list.html',
        {
            'board_list': board_list
        }
    )

def addboard(request):
    if request.method == 'GET':
        return render(request, 'board/addboard.html')
    else:
        title = request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        BoardModel(title=title, writer=writer, content=content).save()
        return HttpResponseRedirect(reverse('board:list'))

def detail(request, id):    
    info = BoardModel.objects.get(id=id)
    info.incrementReadCount()
    return render(
        request,
        'board/detail.html',
        {'info':info}
    )  

def editboard(request, id):
    info = BoardModel.objects.get(id=id)
    if request.method == 'GET':       
        return render(request, 'board/editboard.html', {'info':info})
    elif request.method == 'POST':
        info.title = request.POST['title']
        info.writer = request.POST['writer']
        info.content = request.POST['content']
        info.save()
        return HttpResponseRedirect(reverse('board:list'))
    
def deleteboard(request, id):
    info = BoardModel.objects.get(id=id)
    if request.method == 'GET':       
        return render(request, 'board/deleteboard.html', {'info':info})
    elif request.method == 'POST':
        info.delete()
        return HttpResponseRedirect(reverse('board:list'))
    