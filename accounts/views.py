from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth




def register(request):
   if request.method == 'POST':
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']
      message = validate(username, email, password, password2)
      if(message != ""):         
         messages.error(request, message)
         request.session['firstname'] = firstname
         request.session['lastname'] = lastname
         request.session['username'] = username
         request.session['email'] = email
         return redirect('register') #render(request, 'accounts/register.html', context)
      else:
         user = User.objects.create_user(username = username, email= email,password = password, first_name = firstname, last_name = lastname)
         user.save()
         messages.success(request, 'you are registered successfully, now you can login!')
         return redirect('login')
   else:
      return render(request, 'accounts/register.html') 

def login(request):
   return render(request, 'accounts/login.html')    

def logout(request):
   return redirect('index')

def dashboard(request):
   return render(request, 'accounts/dashboard.html') 


def validate(username, email, password, password2):
   message = ""
   if password != password2:
      message += "the entered passwords don't match! \n"
   elif User.objects.filter(username = username).exists():
      message += "this username is taken! \n"
   elif User.objects.filter(email = email).exists():
      message += "this email exists in database! \n"  
   elif valid_email(email) == False:    
      message += "the email format is not valie! \n"
   return message

import re
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))