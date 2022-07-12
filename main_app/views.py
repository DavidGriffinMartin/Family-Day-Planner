from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event
from .forms import DateForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    date_form = DateForm()
    return render(request, 'dashboard.html', {'date_form': date_form})


def date_detail(request):
    if request.method == 'POST':
        date = DateForm(request.POST)
        if date.is_valid():
            date.save(commit=False)
            date_selected = date.cleaned_data.get('date')
        events = Event.objects.filter(date=date_selected).filter(user=request.user)
        print(request.user)
        return render(request, 'date_detail.html', {'events': events, 'date_selected': date_selected})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            user = form.save()
            login(request, user)
            return redirect('index')
        except:
            error_message = form.errors
            print(form.errors)
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['date', 'name', 'timeBeg', 'timeEnd']
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
      
class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/dashboard'
