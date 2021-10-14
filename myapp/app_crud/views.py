from django.shortcuts import redirect, render
from .forms import PersonForm, CreateUserForm
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# Controlers


@login_required(login_url='/loginUser')
def person_list(request):  # GET
    context = {'person_list': Person.objects.all()}
    return render(request, "app_crud/person_list.html", context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/person')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Se ha creado el nuevo usuario ' + user)
                return redirect('/loginUser')
        context = {'form': form}
        return render(request, 'app_crud/registerUser.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/person')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/person')
            else:
                messages.info(
                    request, 'Las credenciales son incorrectas. Vuelva a ingresar sus credenciales correctamente.')
        context = {}
        return render(request, 'app_crud/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/loginUser')


@login_required(login_url='/loginUser')
def person_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PersonForm()
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(instance=person)
        return render(request, "app_crud/person_form.html", {'form': form})
    else:
        if id == 0:
            form = PersonForm(request.POST)
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return redirect('/list')


@login_required(login_url='/loginUser')
def person_delete(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('/list')
