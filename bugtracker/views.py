from django.shortcuts import render, redirect
from users.forms import BugRegisterForm
from .models import Bug
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    context = {
        'bugs' : Bug.objects.all()
    }
    return render(request, 'bugtracker/home.html', context)

def about(request):
    return render(request, 'bugtracker/about.html')
#
#def registerbug(request):
#    context = {}
#    if request.method == 'POST':
#        form = BugRegisterForm(request.POST)
#        if form.is_valid():
#            form.instance.author = request.user
#            bug = form.save()
#            messages.success(request, f'Your bug has been registered!')
#            return redirect('users-profile')
#    else:
#        form = BugRegisterForm()
#    context['form'] = form
#    return render(request, 'bugtracker/registerbug.html', context)

#def buglist(request):
#    context = {
#        'bugs': Bug.objects.all()
#    }
#    return render(request, 'bugtracker/buglist.html', context)

#def bugdetail(request):
#    return render(request, 'bugtracker/home.html')

class BugListView(ListView):
    model = Bug
    template_name = 'bugtracker/Home.html'
    context_object_name = 'bugs'


class BugDetailView(DetailView):
    model = Bug
    template_name = 'bugtracker/bug-detail.html'


class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['title', 'description']
    template_name = 'bugtracker/registerbug.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BugUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bug
    fields = ['title', 'description', 'status', 'solved_date']
    template_name = 'bugtracker/registerbug.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        bug = self.get_object()
        if str(self.request.user.groups.all()[0]) == 'Programmers':
            return True
        return False


class BugDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bug
    success_url = '/'
    template_name = 'bugtracker/bug-confirm-delete.html'

    def test_func(self):
        bug = self.get_object()
        if str(self.request.user.groups.all()[0]) == 'Programmers':
            return True
        return False
