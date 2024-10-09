from django.http import HttpResponse
from django.shortcuts import render
from task.models import Task
from django.views.generic import DetailView,ListView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from task.forms import createform
from .forms import createform
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import SighnUpForm
from django.views.decorators.csrf import csrf_exempt
from . models import Profile
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.mixins import LoginRequiredMixin
import time



"""def mainpage(request):
    object_list=list(Task.objects.all())
    context={'object_list': object_list}
    return render(request, 'task_page.html', context=context)"""

class mainpage(ListView,LoginRequiredMixin):
    template_name = 'task_page.html'
    model = Task
    context_object_name = "object_list"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        context['count'] = context['object_list'].filter(complete=False).count()

        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['object_list']=context['object_list'].filter(title__icontains=search_input)
        return context


def create_task(request):
    if request.method=="GET":
        form=createform(request.GET)
        return render(request, 'create_page.html', {"form": form})
        return redirect("/mainpage/")

    elif request.method=='POST':
        form = createform(request.POST)
        if form.is_valid():
            obj=form.save()
            obj.user=str(request.user)
            obj.save()
            messages.success(request,("your form was successfully added"))
        else:
            messages.error(request,("failed to save"))
        return redirect("/mainpage/")
    else:
        return redirect("/mainpage/")

def delete_page(request,title):
    if request.method=='GET':
        return render(request,'delete_task.html',{"title":title})
    elif request.method=='POST':
        task = Task.objects.get(title=title)
        task.delete()
        return redirect("/mainpage/")
    else:
        return redirect("/mainpage/")

class Update_task(UpdateView):
    model = Task
    fields = ('title','discription','complete')
    template_name = 'update_page.html'
    def get_success_url(self):
        return reverse_lazy('mainpage')

def show_task(request,title):
    upd=Task.objects.get(title=title)
    return render(request,'show_page.html',{'object':upd})

@csrf_exempt
def signup(request):
    if request.method=="POST":
        form=SighnUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("user creations was successfully")
        return HttpResponse(f"{form.errors}")
    elif request.method=="GET":
        form=SighnUpForm(request.GET)
        return render(request,'signup.html',{'form':form })
    else:
        return redirect("/mainpage/")


class Login(LoginView):
    template_name = 'login.html'
    fields='__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('mainpage')

