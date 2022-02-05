from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'home.html', {'todo_items': todo_items})


def add_todo(request):

    current_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    length_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect("/")


def delete_todo(request, id):
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect('/')
