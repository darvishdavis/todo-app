
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from todoapp_1.form import TaskForm
from todoapp_1.models import TodoDetails

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
#class based views

class TodoListView(ListView):
    model = TodoDetails
    template_name = 'home.html'
    context_object_name = 'info'


class TodoDetailView(DetailView):
    model = TodoDetails
    template_name = 'detail.html'
    context_object_name = 'info'


class TodoUpdateView(UpdateView):
    model = TodoDetails
    template_name = 'update.html'
    context_object_name = 'old'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp_1:c-details', kwargs={'pk': self.object.id})


class TodoDeleteView(DeleteView):
    model = TodoDetails
    template_name = 'delete.html'
    context_object_name = 'dtls'
    extra_context = {'id': id}

class Y(DeleteView):
    model = TodoDetails
    template_name = 'home.html'
    def get_success_url(self):
        return redirect('/')



#function based views

def home(request):
    if request.method == 'POST':
        a = request.POST.get('task')
        b = request.POST.get('priority')
        c = request.POST.get('date')
        TodoDetails(task=a, priority=b, date=c).save()

    information = TodoDetails.objects.all()

    return render(request, 'home.html', {'info': information})


def delete(request, id):
    details = TodoDetails.objects.get(id=id)
    return render(request, 'delete.html', {'dtls': details, 'id':id})

def y(request, id):
    details = TodoDetails.objects.get(id=id)
    details.delete()
    return redirect('/')


def update(request, id):
    old = TodoDetails.objects.get(id=id)
    new = TaskForm(request.POST or None, instance=old) # NB: date field should be updated
    if new.is_valid():
        new.save()
        return redirect('/')
    else:
        return render(request, 'update.html', {'old': old})


