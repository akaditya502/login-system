from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        User = authenticate(username=username,password=pass1)

        if User is not None:
            login(request,User)
            fname = User.first_name
            
            #lname = User.lname_name
            return render(request,"index.html",{'fname':fname})
        else:
            messages.error(request,'bad credential')
            return redirect('home')

    return render(request,"signin.html")
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been created")
        return redirect('/signin')


        

        






    return render(request,'signup.html')
def signout(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('/')
    #return render(request,'signout.html')



