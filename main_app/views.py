from django.shortcuts import render, redirect
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
    return render(request, 'dashboard.html')


# def pick_date (request):
#     date = DateForm(request)
#     return redirect('date_detail.html')


def date_detail(request):
    if request.method == 'POST':
        form = request.POST
        # form.save()
        # date = request.GET.get('date')
        print(form, "hello")
        events = Event.objects.all()
        return render(request, 'date_detail.html', {'events': events})
    else:
        return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
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