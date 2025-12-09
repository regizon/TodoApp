from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTask', views.add_task, name='add_task'),
    path('deleteTask', views.delete_task, name='delete_task'),
    path('updateTask', views.update_task, name='save_task'),
    path('updatePriority', views.update_priority, name='update_priority'),
    path('register', views.register, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('search', views.search, name='search'),
]