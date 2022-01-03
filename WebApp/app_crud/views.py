from django.shortcuts import redirect, render
from .forms import ActivityForm, PersonForm, CreateUserForm
from .models import Activity, Person, Status, Urgency, Category
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


    context = {'person_list':Person.objects.all()}

    return render(request, "app_crud/person_list.html", context)

def activity_list(request):  # GET
    
    context = {'activity_list': Activity.objects.all()}
    return render(request, "app_crud/activity_list.html", context)


def bono_list(request):  # GET
    people = Person.objects.all()
    mapped_people = obtener_bonos(people)
    context = {'person_list': mapped_people }

    return render(request, "app_crud/bono_list.html", context)

def obtener_bonos(people):
    for person in people:
        total_activity_points = 0
        activities = Activity.objects.all()
        person_activities = []
        for activity in activities:
            if str(activity.person) == str(person.name):
                person_activities.append(activity)
        for activity in person_activities:
            total_activity_points += int(activity.points)
            print("Person: " + person.name + " Total Points: " + str(total_activity_points))
        person.person_points = str(total_activity_points)

    people_activities_value = []

    for person in people:
        person.person_activities = Bono_list(person.name)
        if int(person.person_points) >= 15:
            person.person_bonus = True
        people_activities_value.append(Bono_list(person.name))
        print(person.person_bonus)

    return people

def Bono_list(name):
    persona = Person.objects.get(name=Person.objects.get(name=name))
    allActivities={}
    total_activities = 0
    for activity in persona.activity_set.all():
        if activity.person in allActivities:
            allActivities[activity.person] += 1
        else:
            allActivities[activity.person] = 1
        total_activities = allActivities[activity.person] 
    return total_activities

# Bono_list("Sebastian")
# obtener_bonos(people)

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
            updatedActivity = update_progression(activity)
            form = ActivityForm(instance=updatedActivity)
            
        return render(request, "app_crud/activity_form.html", {'form': form})
    else:
        if id == 0:
            form = ActivityForm(request.POST)
        else:
            activity = Activity.objects.get(pk=id)
            updatedActivity = update_progression(activity)
            form = ActivityForm(request.POST, instance=updatedActivity)
            
        if form.is_valid():
            form.save()
        return redirect('/activity_list')

def update_progression(activity):
    categories= Category.objects.all()
    status = Status.objects.all()   
    urgencies = Urgency.objects.all()
    print(urgencies[2].points_urg)
    for stat in status:
        print(stat.status)
        print(activity.status)
        print(str(stat.status) == str(activity.status))
        if (str(stat.status) == str(activity.status)):
            print("Status points:")
            print(stat.points_sts)
            activity.points = int(stat.points_sts)    
    for urgency in urgencies:
        if(str(urgency.urgency) == str(activity.urgency)):
            activity.points += int(urgency.points_urg) 
    for category in categories:
        if(str(category.category_name) == str(activity.category)):
            activity.points += int(category.category_points)
    print(activity.points)
    return activity

@login_required(login_url='/loginUser')
@allowed_users(allowed_roles=['admin'])

def person_delete(id):
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
       
     context={}
     return render(request, 'app_crud/activity_list.html', context)
