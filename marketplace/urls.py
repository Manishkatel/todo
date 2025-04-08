from django.contrib import admin
from django.urls import path, include
from loginsystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('loginsystem.urls')), 
    path('signup/', views.signupuser, name='signupuser'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('home/', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete/', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete/', views.deletetodo, name='deletetodo'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('api/', include('loginsystem.urls')),  # Make sure you add the app's API routes here
]


