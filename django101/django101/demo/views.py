from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from django101.demo.models import Todo


def index(request):
    context = {
        'title': 'Func-based view',
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Class-based view',
        }

        return render(request, 'index.html', context)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'

        return context


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Todos'

        return context


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'todo-details.html'
    context_object_name = 'todo'


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = ('title', 'description', 'category')
