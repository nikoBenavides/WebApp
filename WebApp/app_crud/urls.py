
from django.urls import path, include
from .import views

urlpatterns = [
    path('person/', views.person_form, name='person_insert'),                       #Insert info
    path('<int:id>/', views.person_form,name='person_update'),               #Update info
    path('list/', views.person_list,  name='person_list'),                   #Display record
    path('delete/<int:id>/', views.person_delete , name= 'person_delete'),   #Delete info
    path('registerUser/', views.registerUser, name='registerUser'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('', views.person_form, name='Home'),
    path('user/',views.userPage, name="userPage" )
    

] 