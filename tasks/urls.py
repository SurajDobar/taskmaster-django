# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('task/',views.task,name='task'),
    path('task/<str:tid>',views.task, name='task_filter'),
    path('task/<int:tid>/edit',views.update_task, name="update_task"),
    path('task/<int:tid>/delete',views.delete_task,name="deletetask"),
    path('POSTform/',views.postform, name='POSTform'),

    path('register/',views.register,name='register'),
    path('login/',views.my_login,name='login'),
    path('logout/',views.user_logout,name="user-logout")
]
