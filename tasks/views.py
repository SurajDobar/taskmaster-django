# views.py
from django.shortcuts import render,redirect
from .models import Task
from .forms import POSTform , CreateUserForm ,LoginForm
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'index.html')

@login_required(login_url='login')
def task(request, tid=None):
    tasks = Task.objects.all()

    if tid == "complete":
        tasks = Task.objects.filter(completed=True)

    elif tid == "incomplete":
        tasks = Task.objects.filter(completed=False)

    elif tid and  tid.isdigit():
        tasks = Task.objects.filter(id=int(tid))

    profile_photo = None
    try:
        social_account = request.user.socialaccount_set.get(provider='google')
        profile_photo = social_account.extra_data.get('picture')
    except Exception:
        pass

    display_name = request.user.get_full_name() or request.user.username

    return render(request, "tasks/task.html", {
        "tasks": tasks,
        "tid": tid,
        "profile_photo": profile_photo,
        "display_name": display_name,
    })
def postform(request):
    if request.method=='POST':
        form=POSTform(request.POST)

        if form.is_valid():
            form.save()

    else :
        form=POSTform()

    return render(request,'tasks/POSTform.html',{'form':form})



def delete_task(request,tid):
    if request.method == 'POST':
        Task.objects.filter(id=tid).delete()
    return redirect('task')
    


def update_task(request, tid):
    task = Task.objects.get(id=tid)

    if request.method == 'POST':
        form = POSTform(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task')

    else:
        form = POSTform(instance=task)

    return render(request, 'tasks/update.html', {
        'form': form,
        'task': task
    })



# def register(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']


#         User.objects.create_user(
#             username=username,
#             password=password
#         )
#         return redirect('task')
#     return render(request,'register/login.html')


def register(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('task')
    context = {'registerform':form}
    return render(request , 'register/register.html',context=context)

def my_login(request):
    form =LoginForm()
    if request.method=="POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("task")
    context={'loginform':form}

    return render(request,'register/login.html',context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('register')
