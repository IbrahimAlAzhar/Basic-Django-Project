from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .forms import LoginForm
from django.contrib.auth import authenticate,login

'''
# this method is not work in sqlite3,it works on postgresql,the matching of variable username1 and and register method 
# variable username can not check here

def login(request):
    if request.method == 'POST':
        print("yes")
        username1 = request.POST['username'] # here the username came from login2.html file,you can also bring it from form.py file
        password1 = request.POST['password'] # this password came from html file and store into the variable
        # here red color username and password came from UserFormView(for registration) and the username1 and password1
        # are type the user for login in html file,so we have to verify this
        user = authenticate(username=username1, password=password1)
        if user is not None: # when user is not true
            login(request,user) # this line is use for creating the logout option
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login2.html')
'''


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], # here check the username which one is store in database and cd['username'] which one is came from login form
                                         password=cd['password']) # cd means clean data from form, username and password came from login form
            if user is not None: # user is not none means the user is in database
                if user.is_active:
                    login(request, user) # this line is use for logout option,if u don't need to logout options that u can erase this line
                    return redirect('/') # you should use redirect to '/' page,this one is home page and you have to set this in urls.py file in this directory,if you use render then the url doesn't erase,so it create problems when you login after logout if u using render instead of using redirect

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})  # render means this url included to base url and redirect means erase all base url and create one which one is return


def home(request):
    # this page open request to server for this text for execute,
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, 'home.html', {"title_name": "azhar"}) # here request is using for fetch the data

'''
# for redirecting after login page after successfully logout then you should try this method
def logout_user(request):
    logout(request)
    form = LoginForm
    context = {
    "form": form
    }
    return render(request, 'login.html', context)

'''


def logout_user(request): # in this method there nothing redirect to login page,for that reason we can't use form var.
    logout(request) # this logout works from django auth
    return redirect('/')