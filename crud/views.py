from django.shortcuts import render,redirect
from django.views import View
from crud.forms import TodoForm
from crud.models import Todo


# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"index.html")

class TodoListView(View):
    def get(self,request):
        todolist=Todo.objects.all()
        return render(request,"todoList.html",{"data":todolist})

class AddTodoView(View):
    def get(self,request):
        form=TodoForm()
        context={"form":form}
        return render(request,"addTodo.html",context)
    def post(self,request):
        form_data=TodoForm(data=request.POST)
        if form_data.is_valid():
            title=form_data.cleaned_data.get('title')
            desc=form_data.cleaned_data.get('description')
            Todo.objects.create(title=title,description=desc)
            return redirect('list')
        return render(request,"editTodo.html",{"form":form_data})


class DeleteTodoView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        Todo.objects.get(id=tid).delete()
        return redirect('list')

class EditTodoView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=Todo.objects.get(id=tid)
        form=TodoForm(initial={"title":todo.title,"description":todo.description})
        return render(request,"editTodo.html",{"form":form})
    def post(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=Todo.objects.get(id=tid)
        form_data=TodoForm(data=request.POST)
        if form_data.is_valid():
            title=form_data.cleaned_data.get('title')
            desc=form_data.cleaned_data.get('description')
            todo.title=title
            todo.description=desc
            todo.save()
            return redirect('list')
        return render(request,"editTodo.html",{"form":form_data})


class UpdateStatusView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=Todo.objects.get(id=tid)
        todo.status="Completed"
        todo.save()
        return redirect('list')
