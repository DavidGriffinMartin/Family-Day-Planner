from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event
from .forms import DateForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def users_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})


@login_required
def dashboard(request):
    date_form = DateForm()
    return render(request, 'dashboard.html', {'date_form': date_form})


@login_required
def date_detail(request):
    if request.method == 'POST':
        date = DateForm(request.POST)
        if date.is_valid():
            date.save(commit=False)
            date_selected = date.cleaned_data.get('date')
        events = Event.objects.filter(
            date=date_selected).filter(user=request.user)
        otherevents = Event.objects.filter(
            date=date_selected).exclude(user=request.user)
        users = User.objects.all()
        return render(request, 'date_detail.html', {'events': events, 'otherevents': otherevents, 'date_selected': date_selected, 'users': users})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            user = form.save()
            login(request, user)
            return redirect('dashboard')
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


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['date', 'name', 'timeBeg', 'timeEnd']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/dashboard'
