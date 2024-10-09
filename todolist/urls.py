"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from task.views import mainpage,show_task,create_task,delete_page,Update_task,signup,Login
app_name='task'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/',mainpage.as_view(),name='mainpage'),
    path('showpage/<str:title>/',show_task ,name='show_task'),
    path('createtask/',create_task, name='create_task'),
    path('delete/<str:title>/',delete_page , name='delete_page'),
    path('update/<int:pk>',Update_task.as_view(),name='update_page'),
    path('signup/',signup,name='signup'),
    path('login/',Login.as_view() , name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
]
