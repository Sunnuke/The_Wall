from django.shortcuts import render, redirect, HttpResponse
from  .models import *
# Create your views here.

def wall(request):
    context = {
        'User': User.objects.get(id=request.session['user']),
        'status': request.session['word'],
        'Messages': Message.objects.all()
    }
    return render(request, 'wall.html', context)

def message(request):
    Message.objects.create(
        message=request.POST['message'],
        user=User.objects.get(id=request.session['user'])
    )
    return redirect('/wall')

def comment(request):
    Comment.objects.create(
        message=Message.objects.get(id=int(request.POST['comkey'])),
        user=User.objects.get(id=request.session['user']),
        comment=request.POST['comment']
    )
    return redirect('/wall')

def delete(request):
    c = Message.objects.get(id=request.POST['delkey'])
    c.delete()
    return redirect('/wall')