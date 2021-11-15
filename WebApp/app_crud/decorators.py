from django.http import  HttpResponse, request
from django.shortcuts import redirect
from django.utils.regex_helper import Group

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/person')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Usted no tiene acceso ha esta página.')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
            
        if group == 'employee':
             return redirect('userPage')
        if group == 'admin':
            return view_func (request, *args, **kwargs)
    return wrapper_func