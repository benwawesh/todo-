from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.http import require_POST
from .form import TodoForm
from django.http import HttpResponse

def index(request):
    what=Todo.objects.order_by('id')
    form=TodoForm()
    return render(request, 'index.html', {"what":what, "form":form})

def what_todo(request):
    if request.method=='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form)
            new=Todo(text=request.POST['text'])
            new.save()
    return redirect('doing:index')

def completeTodo(request, id):
    todo=Todo.objects.get(pk=id)
    todo.complete = True
    todo.save()

    return redirect('doing:index')

def deletecompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('doing:index')
def deleteall(request):
    Todo.objects.all().delete()
    return redirect('doing:index')
def delete(request,id):
    item=Todo.objects.get(pk=id)
    item.delete()
    return redirect('doing:index')
def editing(request, id):
    item = Todo.objects.get(pk=id)
    print(item)
    form = TodoForm(request.POST)
    return render(request,'update.html',{'item':item,'form':form})
def update(request, id):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            todo_item = Todo.objects.get(id=id)
            todo_item.text = request.POST['text']
            todo_item.save()
            print("not working")
            return redirect('doing:index')
        else:
            return redirect('doing:editing')





