from prjfinal import settings
from prjfinal import info
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from . import token as token_
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
# Create your views here.


# Create your views here.

####### Fonction de recuperation et de traitement des données en cas de post ###############
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['comfirmpwd']
        if User.objects.filter(username=username):
            messages.error(
                request, 'username already taken please try another.')
            return redirect('register_view')
        if User.objects.filter(email=email):
            messages.error(request, 'This email has an account.')
            return redirect('register_view')
        if len(username) > 10:
            messages.error(
                request, 'Please the username must not be more than 10 character.')
            return redirect('register_view')
        if len(username) < 5:
            messages.error(
                request, 'Please the username must be at leat 5 characters.')
            return redirect('register_view')
        if not username.isalnum():
            messages.error(request, 'username must be alphanumeric')
            return redirect('register_view')

        if password != confirmpwd:
            messages.error(request, 'The password did not match! ')
            return redirect('register_view')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.is_active = False
        my_user.save()
        return redirect('login_view')
        messages.success(
            request, 'Your account has been successfully created. we have sent you an email You must comfirm in order to activate your account.')
# send email when account has been created successfully
        subject = "Welcome to django-application Dylan"
        message = "Welcome " + my_user.first_name + " " + my_user.last_name + \
            "\n thank for chosing Dprogrammeur website for test login.\n To order login you need to comfirm your email account.\n thanks\n\n\n donald programmeur"

        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, effeariel@gmail.com,
                  to_list, fail_silently=False)

# send the the confirmation email
        current_site = get_current_site(request)
        email_suject = "confirm your email DonaldPro Django Login!"
        messageConfirm = render_to_string("emailConfimation.html", {
            'name': my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generateToken.make_token(my_user)
        })

        email = EmailMessage(
            email_suject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
        return redirect('login_view')
    return render(request, "registration/register.html")


# connexion de l'utilisateur
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'message': 'Login failed. Please try again.'})
    else:
        return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')


# déconnexion
def logout_view(request):

    auth.logout(request)

    return redirect('/')


# activation du mail
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_.account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'registration/invalide_token.html')
