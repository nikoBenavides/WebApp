from django.shortcuts import redirect, render
from .forms import ActivityForm, PersonForm, CreateUserForm
from .models import Activity, Person
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import  Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.
# Controlers


@login_required(login_url='/loginUser')
@admin_only
def person_list(request):  # GET
    
    context = {'person_list': Person.objects.all()}
    return render(request, "app_crud/person_list.html", context)

def activity_list(request):  # GET

    context = {'activity_list': Activity.objects.all()}
    return render(request, "app_crud/activity_list.html", context)



@unauthenticated_user
def registerUser(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user= form.save()
                username = form.cleaned_data.get('username')

                group=Group.objects.get(name='employee')
                user.groups.add(group)

                messages.success(
                    request, 'Se ha creado el nuevo usuario ' + username)
                return redirect('/loginUser')
        context = {'form': form}
        return render(request, 'app_crud/registerUser.html', context)

@unauthenticated_user
def loginUser(request):
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
@admin_only
@allowed_users(allowed_roles=['admin'])
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




def activity_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ActivityForm()
        else:
            activity = Activity.objects.get(pk=id)
            form = ActivityForm(instance=activity)
        return render(request, "app_crud/activity_form.html", {'form': form})
    else:
        if id == 0:
            form = ActivityForm(request.POST)
        else:
            activity = Activity.objects.get(pk=id)
            form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
        return redirect('/activity_list')



@login_required(login_url='/loginUser')
@allowed_users(allowed_roles=['admin'])
def person_delete(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('/list')


@login_required(login_url='/loginUser')
@allowed_users(allowed_roles=['admin','employee'])
def activity_delete(request, id):
    activity=Activity.objects.get(pk=id)
    if request.method == "POST":
        activity.delete()
        return redirect('/activity_list')

def userPage(request):
    context = {}
    return render(request, 'app_crud/activity_list.html', context)
