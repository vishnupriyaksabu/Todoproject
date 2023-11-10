from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . models import Task
from . forms import ToDoForm
#  below import statement is used to view all the list by view as a class
from django.views.generic import ListView
from django.views.generic.detail import DetailView
 
from django.views.generic.edit import UpdateView,DeleteView

class Todoclassviewlist(ListView):
    model=Task
    template_name='home.html'
    context_object_name='tasks'

class Todoclassviewdetail(DetailView):
    model=Task
    template_name='details.html'
    context_object_name='task'

class Todoclassviewupdate(UpdateView):
    model=Task
    template_name='edit.html'
    context_object_name='task'
    fields=('Name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
    

class Todoclassviewdelete(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')




# Create your views here.

def add(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        Name=request.POST.get('task','')
        priority=request.POST.get('Priority','')
        date=request.POST.get('date','')
        task=Task(Name=Name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'tasks':tasks})


# function for showing values in details.html page
# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,task_id):
    task=Task.objects.get(id=task_id)
    f=ToDoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})
     

