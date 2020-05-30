from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
'''
# you can't sign up or registration using this method.because when you create a object in database then the parameter username,
# first_name,last_name are same as in user model which locate in postgresql.In sqlite3 there are no oppurtunity to matching this 
# parameter from user models.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username'] # create a variable username and store the value from html file
        firstname = request.POST['first_name'] # store the value of first_name from html file
        lastname = request.POST['last_name'] # her the last_name is the name of this attribute
        email = request.POST['email_id']
        password = request.POST['password']

        x = User.objects.create_user(username = username,first_name=firstname,last_name=lastname,email=email, password= password)
        x.save()
        print("user created successfully")
        redirect('/')
    return render(request,'signup.html')

'''

# in django sqlit3 you if u use registration form,then you have to do this format,
# this is class based view


class UserFormView(View):  # for registration and then login this user automatically
    form_class = UserForm # the user form which is in forms.py file
    template_name = 'registration.html'

    # display blank form: you don't need to write condition of get,post
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False) # here create a instance of form,but not save in database
            username = form.cleaned_data['username']  # cleaned_data of username passed to username variable
            password = form.cleaned_data['password'] # cleaned data represent the fresh value from form
            user.set_password(password) # password set using function,because password is not a plain text
            user.save()

            # returns User objects if credentials are correct (for authentication)
            user = authenticate(username=username, password=password) # take the username and password
            if user is not None:  # if the user is exist in admin database
                if user.is_active:
                    login(request, user)  # login automatically if all conditions are ok
                    print("account created successfully")
                    return render(request, 'home.html',{'new_user': user}) # after successfully login then the index page redirect
        return render(request, self.template_name, {'form': form})  # if form is not valid or user is not register in database then redirect the same registration form


def register_done(request):
    return render(request, "register_done.html")