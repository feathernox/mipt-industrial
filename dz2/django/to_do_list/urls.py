from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login_view'),
    path('login_action', views.login_action, name='login_action'),
    path('signup', views.signup_view, name='signup_view'),
    path('signup_action', views.signup_action, name='signup_action'),
    path('todolist', views.todolist_view, name='todolist_view'),
    path('todolist_action_add', views.todolist_action_add,
         name='todolist_action_add'),
    path('todolist_action_update', views.todolist_action_update,
         name='todolist_action_update'),
    path('logout_action', views.logout_action, name='logout_action'),
]
