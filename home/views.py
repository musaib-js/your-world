from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Services, Contact
from django.core.mail import send_mail

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    allServices = Services.objects.all()
    context = {'allServices': allServices}
    return render(request, 'services.html', context)

def service(request, slug):
     service = Services.objects.filter(slug=slug)[0]
     service.save()
     context = {'service' : service}
     return render(request, 'service.html', context)


def contact(request):
    if request.method == "POST":
        #Get the Contact Parameters

        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        concern = request.POST['concern']
        details = request.POST['details']

        # Save the Parameters To the Database
        contact = Contact(name = name, phone = phone, email = email, concern = concern, details = details)
        contact.save()

         #Send the Data Via Email
        fromemail = 'submissions.yf@gmail.com'
        subject = "New Anonymous Submission"
        message = "Name: " + name + '\n' + "Phone: " + phone + '\n' + "Email: " +  email + '\n' + "Concern: " + concern + '\n' + "Details: " + details 

        send_mail(subject, message, fromemail, ['submissions.yf@gmail.com'])
        messages.success(request, "Your Details Have Been Submittted Successfully. We'll Get Back To You Soon")
        
    return render(request, 'contact.html')

def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.error(request, " Your user name must of atleast 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your YF! has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

    return HttpResponse("login")

def handleLogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')


    return HttpResponse("Login")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')



